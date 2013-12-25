
package ;

import js.Browser;
import js.Lib;

using StringTools;


@:expose
class Social
{
    static function main() { }
/*
    @url = page url
    @text = main text
    @via = from user
    @related = related account
*/
    @:keep public static function twitter(title=''): js.html.AnchorElement
    {
        var my_url = Browser.location.href;
        var title_sentence =
            if (title == '')
                {
                    var t: Dynamic = Browser.document.getElementsByTagName("title")[0];
                    t.innerText;
                }
            else title;
        var params = 'url=${my_url.urlEncode()}&text=${title_sentence}';
        var ref_to_myarticle = 'http://twitter.com/share?${params}';
        var ancor_to_twitter = Browser.document.createAnchorElement();
        ancor_to_twitter.href = ref_to_myarticle;
        ancor_to_twitter.setAttribute('target', '_blank');
        return ancor_to_twitter;
    }
}
