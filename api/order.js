exports.GET = function(args) {
    // access VS Code API (s. https://code.visualstudio.com/Docs/extensionAPI/vscode-api)
    var vscode = require('vscode');

    // access Node.js API provided by VS Code
    // s.  (s. https://nodejs.org/api/)
    var fs = require('fs');

    // access an own module
    var myModule = require('./my-module.js');

    // access a module used by the extension:
    // s. https://mkloubert.github.io/vs-rest-api/modules/_helpers_.html
    var helpers = args.require('./helpers');
    // s. https://mkloubert.github.io/vs-rest-api/modules/_host_helpers_.html
    var hostHelpers = args.require('./host/helpers');

    // access a module that is part of the extentsion
    // s. https://github.com/mkloubert/vs-rest-api/blob/master/package.json
    var glob = args.require('glob');

    // access the data from the settings
    // from the example above this is: "Hello!"
    var opts = args.options;

    // share / store data (while current session)...
    // ... for this script
    var myState = args.state;
    args.state = new Date();
    // ... with other scripts of this type
    args.globalState['myEndpoint'] = new Date();
    // ... with the whole workspace
    args.workspaceState['myEndpoint'] = new Date();

    // if you want to return an AJAX response object:
    // s. https://mkloubert.github.io/vs-rest-api/interfaces/_contracts_.apiresponse.html
    {
        args.response.code = 666;  // the response code (not the HTTP response code!)
        args.response.msg = 'Result of the evil!';  // a custom message for more information
        args.response.data = {
            id: 1,
            name: 'James',
            drink: 'Coffee'
          },
          {
            id: 2,
            name: 'John',
            drink: 'Latte'
          };
    }

    // if you want to return custom content
    // instead of the object in 'args.response'
    // s. https://mkloubert.github.io/vs-rest-api/interfaces/_contracts_.apimethodarguments.html#setcontent
    {
        var html = fs.readFileSync('/path/to/my/file.html');

        // open HTML document in new tab (for reports e.g.)
        args.openHtml(html.toString('utf8'), 'My HTML document from "file.html"').then(function() {
            // HTML opened
        }, function(err) {
            // opening HTML document failed
        });

        args.setContent(html, 'text/html');
    }

    // deploys 'index.html' to 'My SFTP server'
    // s. https://github.com/mkloubert/vs-deploy
    args.deploy(['./index.html'], ['My SFTP server']).then(function() {
        // file deployed
    }, function(err) {
        // deployment failed
    });

    // custom HTTP status code
    args.statusCode = 202;

    // ...
}