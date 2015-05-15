System.config({
  "baseURL": "/nm/",
  "transpiler": "babel",
  "paths": {
    "babel": "/nm/babel-core/browser.min.js",
    "react/addons": "/nm/react/dist/react-with-addons.min.js",
    "react": "/nm/react/dist/react.min.js",
    "jQuery": "/nm/jquery/dist/jquery.min.js",

    "app/*": "/static/app/*.js",
    "store/*": "/static/store/*.js"
  },
  "map": {
    "URIjs": "/nm/URIjs/src/URI",
    "flux": "/nm/flux/index"
  },
  "babelOptions": {
    "optional": ["runtime"],
    "blacklist": []
  }
});
