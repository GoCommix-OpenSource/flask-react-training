const path = require('path');
const webpack = require('webpack');
module.exports={
    entry:path.resolve(__dirname,"/src/index.js"),
    output:{
        path:path.resolve(__dirname,"../backend/static"),
        filename:"[name].js"
    },
    module:{
        rules:[
            {
                test:/\.js|.jsx$/,
                exclude:/node_modules/,
                use:'babel-loader'
            }
        ]
    },
    // experiments: {
    //     outputModule: true,
    // },
    output: {
        asyncChunks: true,
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: JSON.stringify("development"),
            },
        }),
    ],
    
}