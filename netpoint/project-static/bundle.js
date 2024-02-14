const esbuild = require('esbuild');
const { sassPlugin } = require('esbuild-sass-plugin');

// Bundler options common to all bundle jobs.
const options = {
  outdir: './dist',
  bundle: true,
  minify: true,
  sourcemap: 'external',
  sourcesContent: false,
  logLevel: 'error',
};

// Get CLI arguments for optional overrides.
const ARGS = process.argv.slice(2);

async function bundleGraphIQL() {
  try {
    const result = await esbuild.build({
      ...options,
      entryPoints: {
        graphiql: 'netpoint-graphiql/index.ts',
      },
      target: 'es2016',
      define: {
        global: 'window',
      },
    });
    if (result.errors.length === 0) {
      console.log(`✅ Bundled source file 'netpoint-graphiql/index.ts' to 'graphiql.js'`);
    }
  } catch (err) {
    console.error(err);
  }
}

/**
 * Bundle Core NetPoint JavaScript.
 */
async function bundleNetPoint() {
  const entryPoints = {
    netpoint: 'src/index.ts',
  };
  try {
    const result = await esbuild.build({
      ...options,
      entryPoints,
      target: 'es2016',
    });
    if (result.errors.length === 0) {
      for (const [targetName, sourceName] of Object.entries(entryPoints)) {
        const source = sourceName.split('/')[1];
        console.log(`✅ Bundled source file '${source}' to '${targetName}.js'`);
      }
    }
  } catch (err) {
    console.error(err);
  }
}

/**
 * Run script bundle jobs.
 */
async function bundleScripts() {
  for (const bundle of [bundleNetPoint, bundleGraphIQL]) {
    await bundle();
  }
}

/**
 * Run style bundle jobs.
 */
async function bundleStyles() {
  try {
    const entryPoints = {
      'netpoint-external': 'styles/_external.scss',
      'netpoint-light': 'styles/_light.scss',
      'netpoint-dark': 'styles/_dark.scss',
      'netpoint-print': 'styles/_print.scss',
      rack_elevation: 'styles/_rack_elevation.scss',
      cable_trace: 'styles/_cable_trace.scss',
      graphiql: 'netpoint-graphiql/graphiql.scss',
    };
    const pluginOptions = { outputStyle: 'compressed' };
    // Allow cache disabling.
    if (ARGS.includes('--no-cache')) {
      pluginOptions.cache = false;
    }
    let result = await esbuild.build({
      ...options,
      // Disable sourcemaps for CSS/SCSS files, see #7068
      sourcemap: false,
      entryPoints,
      plugins: [sassPlugin(pluginOptions)],
      loader: {
        '.eot': 'file',
        '.woff': 'file',
        '.woff2': 'file',
        '.svg': 'file',
        '.ttf': 'file',
      },
    });
    if (result.errors.length === 0) {
      for (const [targetName, sourceName] of Object.entries(entryPoints)) {
        const source = sourceName.split('/')[1];
        console.log(`✅ Bundled source file '${source}' to '${targetName}.css'`);
      }
    }
  } catch (err) {
    console.error(err);
  }
}

/**
 * Run all bundle jobs.
 */
async function bundleAll() {
  if (ARGS.includes('--styles')) {
    // Only run style jobs.
    return await bundleStyles();
  } else if (ARGS.includes('--scripts')) {
    // Only run script jobs.
    return await bundleScripts();
  }
  await bundleStyles();
  await bundleScripts();
}

bundleAll();
