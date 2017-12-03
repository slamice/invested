var webpack = require('webpack');
var path = require('path');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var AssetsPlugin = require('assets-webpack-plugin');
var cssnext = require('postcss-cssnext');

module.exports = {
    entry: {
        main: "./js/main.jsx"
    },
    output: {
        path: path.resolve(__dirname, 'static'),
        publicPath: "/static/",
        filename: 'scripts/[name]-bundle-[hash].js'
    },
    resolve: {
        extensions: [
            '.jsx', '.js', '.json'
        ],
        modules: [
            'node_modules',
            path.resolve(__dirname, './node_modules')
        ]
    },
    module: {
        loaders: [
            {
                test: /\.css$/,
                use: [require.resolve('style-loader'), 'css-loader?url-loader?sourceMap&modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]', require.resolve('postcss-loader')]
            }, {
                test: /(\.js|\.jsx)$/,
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'stage-0', 'react']
                }
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin('styles/main-bundle-[hash].css'),
        new AssetsPlugin()
    ]
};
