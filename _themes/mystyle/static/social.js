(function () { "use strict";
var Main = function() { }
Main.main = function() {
}
var Social = function() { }
$hxExpose(Social, "Social");
Social.main = function() {
}
Social.twitter = function(title) {
	if(title == null) title = "";
	var my_url = js.Browser.location.href;
	var title_sentence = title == ""?(function($this) {
		var $r;
		var t = js.Browser.document.getElementsByTagName("title")[0];
		$r = t.innerText;
		return $r;
	}(this)):title;
	var params = "url=" + StringTools.urlEncode(my_url) + "&text=" + title_sentence;
	var ref_to_myarticle = "http://twitter.com/share?" + params;
	var ancor_to_twitter = js.Browser.document.createElement("a");
	ancor_to_twitter.href = ref_to_myarticle;
	ancor_to_twitter.setAttribute("target","_blank");
	return ancor_to_twitter;
}
var StringTools = function() { }
StringTools.urlEncode = function(s) {
	return encodeURIComponent(s);
}
var js = {}
js.Browser = function() { }
js.Browser.document = typeof window != "undefined" ? window.document : null;
js.Browser.location = typeof window != "undefined" ? window.location : null;
Main.main();
function $hxExpose(src, path) {
	var o = typeof window != "undefined" ? window : exports;
	var parts = path.split(".");
	for(var ii = 0; ii < parts.length-1; ++ii) {
		var p = parts[ii];
		if(typeof o[p] == "undefined") o[p] = {};
		o = o[p];
	}
	o[parts[parts.length-1]] = src;
}
})();
