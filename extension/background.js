// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// const tab_log = function(json_args) {
//   var args = JSON.parse(unescape(json_args));
//   console[args[0]].apply(console, Array.prototype.slice.call(args, 1));
// }


// chrome.extension.onRequest.addListener(function(request) {
// 	console.log('REQUEST  CAUGHT ');
// 	console.log('REQUEST  CAUGHT ' +request);
//   if (request.command !== 'sendToConsole')
//     return;
//   chrome.tabs.executeScript(request.tabId, {
//       code: "("+ tab_log + ")('" + request.args + "');",
//   });
// });

chrome.extension.onRequest.addListener(
    function(request) {
      // chrome.experimental.devtools.console.addMessage(
      //     chrome.experimental.devtools.console.Severity.Warning,
      //     "Large image: " + request.request.url);
	  chrome.extension.getBackgroundPage().console.log('foo');
      console.log('here');
      document.getElementById('main').innerHTML = 'HEY';
});

chrome.extension.getBackgroundPage().console.log('foo');

chrome.webRequest.onBeforeSendHeaders.addListener(
    function(details) {
    	chrome.extension.getBackgroundPage().console.log(details);
        details.requestHeaders.push({name:"dummyHeader",value:"1"});
        return {requestHeaders: details.requestHeaders};
    },
    {urls: ["<all_urls>"]},
    ["requestHeaders", "blocking"]
                      //^^^^^^^^
);

// chrome.webRequest.onCompleted.addListener(
//   callback, filter, opt_extraInfoSpec);