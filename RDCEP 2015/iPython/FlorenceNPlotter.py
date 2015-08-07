<!DOCTYPE html>
<html lang="en" >

<head>
	<noscript><meta http-equiv="refresh" content="0; URL=/files/bglick/F073J3BSL/florencenplotter.py?nojsmode=1" /></noscript>
<script type="text/javascript">
window.load_start_ms = new Date().getTime();
window.load_log = [];
window.logLoad = function(k) {
	var ms = new Date().getTime();
	window.load_log.push({
		k: k,
		t: (ms-window.load_start_ms)/1000
	})
}
if(self!==top)window.document.write("\u003Cstyle>body * {display:none !important;}\u003C\/style>\u003Ca href=\"#\" onclick="+
"\"top.location.href=window.location.href\" style=\"display:block !important;padding:10px\">Go to Slack.com\u003C\/a>");
</script>


<script type="text/javascript">
window.callSlackAPIUnauthed = function(method, args, callback) {
	var url = '/api/'+method+'?t='+new Date().getTime();
	var req = new XMLHttpRequest();
	
	req.onreadystatechange = function() {
		if (req.readyState == 4) {
			req.onreadystatechange = null;
			var obj;
			
			if (req.status == 200) {
				if (req.responseText.indexOf('{') == 0) {
					try {
						eval('obj = '+req.responseText);
					} catch (err) {
						console.warn('unable to do anything with api rsp');
					}
				}
			}
			
			obj = obj || {
				ok: false	
			}
			
			callback(obj.ok, obj, args);
		}
	}
	
	req.open('POST', url, 1);
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

	var args2 = [];
	for (i in args) {
		args2[args2.length] = encodeURIComponent(i)+'='+encodeURIComponent(args[i]);
	}

	req.send(args2.join('&'));
}
</script>

			
	
	<script type="text/javascript">

		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
		ga('create', 'UA-106458-17', 'slack.com');
		ga('send', 'pageview');

		
		(function(e,c,b,f,d,g,a){e.SlackBeaconObject=d;
		e[d]=e[d]||function(){(e[d].q=e[d].q||[]).push([1*new Date(),arguments])};
		e[d].l=1*new Date();g=c.createElement(b);a=c.getElementsByTagName(b)[0];
		g.async=1;g.src=f;a.parentNode.insertBefore(g,a)
		})(window,document,"script","https://slack.global.ssl.fastly.net/dcf8/js/libs/beacon.js","sb");
		sb('set', 'token', '3307f436963e02d4f9eb85ce5159744c');

					sb('set', 'user_id', 'U07034TR9');
							sb('set', 'user_batch', "immediate-launch");
							sb('set', 'user_created', "2015-06-29");
						sb('set', 'name_tag', 'rdcep-summer/ncdanica');
				sb('track', 'pageview');

		function track(a){ga('send','event','web',a);sb('track',a);}

	</script>


<script type='text/javascript'>
				
		(function(f,b){if(!b.__SV){var a,e,i,g;window.mixpanel=b;b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");
		for(g=0;g<i.length;g++)f(c,i[g]);b._i.push([a,e,d])};b.__SV=1.2;a=f.createElement("script");a.type="text/javascript";a.async=!0;a.src="//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";e=f.getElementsByTagName("script")[0];e.parentNode.insertBefore(a,e)}})(document,window.mixpanel||[]);
		
		mixpanel.init("12d52d8633a5b432975592d13ebd3f34");
	
	function mixpanel_track(event_name){if(window.mixpanel&&event_name)mixpanel.track(event_name);}
</script>	
			<meta name="referrer" content="no-referrer">
			<meta name="superfish" content="nofish">
	<script type="text/javascript">



var TS_last_log_date = null;
var TSMakeLogDate = function() {
	var date = new Date();

	var y = date.getFullYear();
	var mo = date.getMonth()+1;
	var d = date.getDate();

	var time = {
	  h: date.getHours(),
	  mi: date.getMinutes(),
	  s: date.getSeconds(),
	  ms: date.getMilliseconds()
	};

	Object.keys(time).map(function(moment, index) {
		if(time[moment] < 10) {
			time[moment] = '0' + time[moment];
		}
	});

	var str = y + '/' + mo + '/' + d + ' ' + time.h + ':' + time.mi + ':' + time.s + '.' + time.ms;
	if (TS_last_log_date) {
		var diff = date-TS_last_log_date;
		//str+= ' ('+diff+'ms)';
	}
	TS_last_log_date = date;
	return str+' ';
}

var TSSSB = {
	

	call: function() {
		return false;
	}

	
}

</script>	<script type="text/javascript">
		
		var was_TS = window.TS;
		delete window.TS;
		TSSSB.call('didFinishLoading');
		if (was_TS) window.TS = was_TS;
	</script>
	    <meta charset="utf-8">
    <title>FlorenceNPlotter.py | rdcep-summer Slack</title>
    <meta name="author" content="Slack">

	
						
																						
				
	
		
		<!-- output_css "core" -->
    <link href="https://slack.global.ssl.fastly.net/5e1e/style/rollup-plastic.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/ef0f/style/services.css" rel="stylesheet" type="text/css">

	<!-- output_css "regular" -->
    <link href="https://slack.global.ssl.fastly.net/baa89/style/comments.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/f088f/style/stars.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/15f8/style/rxns.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/0d2e7/style/print.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/f010/style/files.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/1d8a/style/libs/codemirror.css" rel="stylesheet" type="text/css">
    <link href="https://slack.global.ssl.fastly.net/1e63/style/libs/lato-1.css" rel="stylesheet" type="text/css">

	

	
	
	

	<!--[if lt IE 9]>
	<script src="https://slack.global.ssl.fastly.net/ef0d/js/libs/html5shiv.js"></script>
	<![endif]-->

	
<link id="favicon" rel="shortcut icon" href="https://slack.global.ssl.fastly.net/272a/img/icons/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png" />

<link rel="icon" href="https://slack.global.ssl.fastly.net/ba3c/img/icons/app-256.png" sizes="256x256" type="image/png" />

<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-152.png" />
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-144.png" />
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-120.png" />
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-114.png" />
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-72.png" />
<link rel="apple-touch-icon-precomposed" href="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-57.png" />

<meta name="msapplication-TileColor" content="#FFFFFF" />
<meta name="msapplication-TileImage" content="https://slack.global.ssl.fastly.net/272a/img/icons/app-144.png" />	<script>
!function(a,b){function c(a,b){try{if("function"!=typeof a)return a;if(!a.bugsnag){var c=e();a.bugsnag=function(d){if(b&&b.eventHandler&&(u=d),v=c,!y){var e=a.apply(this,arguments);return v=null,e}try{return a.apply(this,arguments)}catch(f){throw l("autoNotify",!0)&&(x.notifyException(f,null,null,"error"),s()),f}finally{v=null}},a.bugsnag.bugsnag=a.bugsnag}return a.bugsnag}catch(d){return a}}function d(){B=!1}function e(){var a=document.currentScript||v;if(!a&&B){var b=document.scripts||document.getElementsByTagName("script");a=b[b.length-1]}return a}function f(a){var b=e();b&&(a.script={src:b.src,content:l("inlineScript",!0)?b.innerHTML:""})}function g(b){var c=l("disableLog"),d=a.console;void 0===d||void 0===d.log||c||d.log("[Bugsnag] "+b)}function h(b,c,d){if(d>=5)return encodeURIComponent(c)+"=[RECURSIVE]";d=d+1||1;try{if(a.Node&&b instanceof a.Node)return encodeURIComponent(c)+"="+encodeURIComponent(r(b));var e=[];for(var f in b)if(b.hasOwnProperty(f)&&null!=f&&null!=b[f]){var g=c?c+"["+f+"]":f,i=b[f];e.push("object"==typeof i?h(i,g,d):encodeURIComponent(g)+"="+encodeURIComponent(i))}return e.join("&")}catch(j){return encodeURIComponent(c)+"="+encodeURIComponent(""+j)}}function i(a,b){if(null==b)return a;a=a||{};for(var c in b)if(b.hasOwnProperty(c))try{a[c]=b[c].constructor===Object?i(a[c],b[c]):b[c]}catch(d){a[c]=b[c]}return a}function j(a,b){a+="?"+h(b)+"&ct=img&cb="+(new Date).getTime();var c=new Image;c.src=a}function k(a){var b={},c=/^data\-([\w\-]+)$/;if(a)for(var d=a.attributes,e=0;e<d.length;e++){var f=d[e];if(c.test(f.nodeName)){var g=f.nodeName.match(c)[1];b[g]=f.value||f.nodeValue}}return b}function l(a,b){C=C||k(J);var c=void 0!==x[a]?x[a]:C[a.toLowerCase()];return"false"===c&&(c=!1),void 0!==c?c:b}function m(a){return a&&a.match(D)?!0:(g("Invalid API key '"+a+"'"),!1)}function n(b,c){var d=l("apiKey");if(m(d)&&A){A-=1;var e=l("releaseStage"),f=l("notifyReleaseStages");if(f){for(var h=!1,k=0;k<f.length;k++)if(e===f[k]){h=!0;break}if(!h)return}var n=[b.name,b.message,b.stacktrace].join("|");if(n!==w){w=n,u&&(c=c||{},c["Last Event"]=q(u));var o={notifierVersion:H,apiKey:d,projectRoot:l("projectRoot")||a.location.protocol+"//"+a.location.host,context:l("context")||a.location.pathname,userId:l("userId"),user:l("user"),metaData:i(i({},l("metaData")),c),releaseStage:e,appVersion:l("appVersion"),url:a.location.href,userAgent:navigator.userAgent,language:navigator.language||navigator.userLanguage,severity:b.severity,name:b.name,message:b.message,stacktrace:b.stacktrace,file:b.file,lineNumber:b.lineNumber,columnNumber:b.columnNumber,payloadVersion:"2"},p=x.beforeNotify;if("function"==typeof p){var r=p(o,o.metaData);if(r===!1)return}return 0===o.lineNumber&&/Script error\.?/.test(o.message)?g("Ignoring cross-domain script error. See https://bugsnag.com/docs/notifiers/js/cors"):(j(l("endpoint")||G,o),void 0)}}}function o(){var a,b,c=10,d="[anonymous]";try{throw new Error("")}catch(e){a="<generated>\n",b=p(e)}if(!b){a="<generated-ie>\n";var f=[];try{for(var h=arguments.callee.caller.caller;h&&f.length<c;){var i=E.test(h.toString())?RegExp.$1||d:d;f.push(i),h=h.caller}}catch(j){g(j)}b=f.join("\n")}return a+b}function p(a){return a.stack||a.backtrace||a.stacktrace}function q(a){var b={millisecondsAgo:new Date-a.timeStamp,type:a.type,which:a.which,target:r(a.target)};return b}function r(a){if(a){var b=a.attributes;if(b){for(var c="<"+a.nodeName.toLowerCase(),d=0;d<b.length;d++)b[d].value&&"null"!=b[d].value.toString()&&(c+=" "+b[d].name+'="'+b[d].value+'"');return c+">"}return a.nodeName}}function s(){z+=1,a.setTimeout(function(){z-=1})}function t(a,b,c){var d=a[b],e=c(d);a[b]=e}var u,v,w,x={},y=!0,z=0,A=10;x.noConflict=function(){return a.Bugsnag=b,x},x.refresh=function(){A=10},x.notifyException=function(a,b,c,d){b&&"string"!=typeof b&&(c=b,b=void 0),c||(c={}),f(c),n({name:b||a.name,message:a.message||a.description,stacktrace:p(a)||o(),file:a.fileName||a.sourceURL,lineNumber:a.lineNumber||a.line,columnNumber:a.columnNumber?a.columnNumber+1:void 0,severity:d||"warning"},c)},x.notify=function(b,c,d,e){n({name:b,message:c,stacktrace:o(),file:a.location.toString(),lineNumber:1,severity:e||"warning"},d)};var B="complete"!==document.readyState;document.addEventListener?(document.addEventListener("DOMContentLoaded",d,!0),a.addEventListener("load",d,!0)):a.attachEvent("onload",d);var C,D=/^[0-9a-f]{32}$/i,E=/function\s*([\w\-$]+)?\s*\(/i,F="https://notify.bugsnag.com/",G=F+"js",H="2.4.7",I=document.getElementsByTagName("script"),J=I[I.length-1];if(a.atob){if(a.ErrorEvent)try{0===new a.ErrorEvent("test").colno&&(y=!1)}catch(K){}}else y=!1;if(l("autoNotify",!0)){t(a,"onerror",function(b){return function(c,d,e,g,h){var i=l("autoNotify",!0),j={};!g&&a.event&&(g=a.event.errorCharacter),f(j),v=null,i&&!z&&n({name:h&&h.name||"window.onerror",message:c,file:d,lineNumber:e,columnNumber:g,stacktrace:h&&p(h)||o(),severity:"error"},j),b&&b(c,d,e,g,h)}});var L=function(a){return function(b,d){if("function"==typeof b){b=c(b);var e=Array.prototype.slice.call(arguments,2);return a(function(){b.apply(this,e)},d)}return a(b,d)}};t(a,"setTimeout",L),t(a,"setInterval",L),a.requestAnimationFrame&&t(a,"requestAnimationFrame",function(a){return function(b){return a(c(b))}}),a.setImmediate&&t(a,"setImmediate",function(a){return function(){var b=Array.prototype.slice.call(arguments);return b[0]=c(b[0]),a.apply(this,b)}}),"EventTarget Window Node ApplicationCache AudioTrackList ChannelMergerNode CryptoOperation EventSource FileReader HTMLUnknownElement IDBDatabase IDBRequest IDBTransaction KeyOperation MediaController MessagePort ModalWindow Notification SVGElementInstance Screen TextTrack TextTrackCue TextTrackList WebSocket WebSocketWorker Worker XMLHttpRequest XMLHttpRequestEventTarget XMLHttpRequestUpload".replace(/\w+/g,function(b){var d=a[b]&&a[b].prototype;d&&d.hasOwnProperty&&d.hasOwnProperty("addEventListener")&&(t(d,"addEventListener",function(a){return function(b,d,e,f){return d&&d.handleEvent&&(d.handleEvent=c(d.handleEvent,{eventHandler:!0})),a.call(this,b,c(d,{eventHandler:!0}),e,f)}}),t(d,"removeEventListener",function(a){return function(b,d,e,f){return a.call(this,b,d,e,f),a.call(this,b,c(d),e,f)}}))})}a.Bugsnag=x,"function"==typeof define&&define.amd?define([],function(){return x}):"object"==typeof module&&"object"==typeof module.exports&&(module.exports=x)}(window,window.Bugsnag);
Bugsnag.apiKey = "2a86b308af5a81d2c9329fedfb4b30c7";
Bugsnag.appVersion = "5d62333be5c79b01b3ed343ad8a67cf1d526a47c-1435783475";
Bugsnag.endpoint = "https://errors.slack-core.com/js";
Bugsnag.releaseStage = "prod";
Bugsnag.autoNotify = false;
Bugsnag.user = {id:"U07034TR9",name:"ncdanica",email:"ncdanica@gmail.com"};
Bugsnag.metaData = {};
Bugsnag.metaData.team = {id:"T06BZ0F60",name:"rdcep-summer",domain:"rdcep-summer"};
Bugsnag.refresh_interval = setInterval(function () { (window.TS && window.TS.client) ? Bugsnag.refresh() : clearInterval(Bugsnag.refresh_interval); }, 15 * 60 * 1000);
</script>
</head>

<body class="">

		  			<script>
		
			var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
			if (w > 1440) document.querySelector('body').classList.add('widescreen');
		
		</script>
	
  	
	

			<nav id="site_nav" class="no_transition">

	<div id="site_nav_contents">

		<div id="user_menu">
			<div id="user_menu_contents">
				<div id="user_menu_avatar">
										<span class="member_image thumb_48" style="background-image: url('https://secure.gravatar.com/avatar/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023.png')" data-thumb-size="48" data-member-id="U07034TR9"></span>
					<span class="member_image thumb_36" style="background-image: url('https://secure.gravatar.com/avatar/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-72.png')" data-thumb-size="36" data-member-id="U07034TR9"></span>
				</div>
				<h3>Signed in as</h3>
				<span id="user_menu_name">ncdanica</span>
			</div>
		</div>

		<div class="nav_contents">

			<ul class="primary_nav">
				<li><a href="/home"><i class="ts_icon ts_icon_home"></i>Home</a></li>
				<li><a href="/account"><i class="ts_icon ts_icon_user"></i>Account & Profile</a></li>
				<li><a href="/services/new"><i class="ts_icon ts_icon_wrench"></i>Integrations</a></li>
				<li><a href="/archives"><i class="ts_icon ts_icon_inbox"></i>Message Archives</a></li>
				<li><a href="/files"><i class="ts_icon ts_icon_file"></i>Files</a></li>
				<li><a href="/team"><i class="ts_icon ts_icon_team_directory"></i>Team Directory</a></li>
									<li><a href="/stats"><i class="ts_icon ts_icon_dashboard"></i>Statistics</a></li>
													<li><a href="/customize"><i class="ts_icon ts_icon_magic"></i>Customize</a></li>
													<li><a href="/account/team"><i class="ts_icon ts_icon_cog_o"></i>Team Settings</a></li>
							</ul>

			
		</div>

		<div id="footer">

			<ul id="footer_nav">
				<li><a href="/is">Tour</a></li>
				<li><a href="/apps">Apps</a></li>
				<li><a href="/brand-guidelines">Brand Guidelines</a></li>
				<li><a href="/help">Help</a></li>
				<li><a href="https://api.slack.com" target="_blank">API<i class="ts_icon ts_icon_external_link small_left_margin"></i></a></li>
								<li><a href="/pricing">Pricing</a></li>
				<li><a href="/help/requests/new">Contact</a></li>
				<li><a href="/terms-of-service">Policies</a></li>
				<li><a href="http://slackhq.com/" target="_blank">Our Blog</a></li>
				<li><a href="https://slack.com/signout/6407015204?crumb=s-1435784600-24fcfc5d1c-%E2%98%83">Sign Out<i class="ts_icon ts_icon_sign_out small_left_margin"></i></a></li>
			</ul>

			<p id="footer_signature">Made with <i class="ts_icon ts_icon_heart"></i> by Slack</p>

		</div>

	</div>
</nav>	
			<header>
							<a id="menu_toggle" class="no_transition">
					<span class="menu_icon"></span>
					<span class="menu_label">Menu</span>
					<span class="vert_divider"></span>
				</a>
				<h1 id="header_team_name" class="inline_block no_transition">
					<a href="/home">
						<i class="ts_icon ts_icon_home" /></i>
						rdcep-summer
					</a>
				</h1>
				<div class="header_nav">
					<div class="header_btns float_right">
						<a id="team_switcher">
							<i class="ts_icon ts_icon_th_large ts_icon_inherit"></i>
							<span class="block label">Teams</span>
						</a>
						<a href="/help" id="help_link">
							<i class="ts_icon ts_icon_life_ring ts_icon_inherit"></i>
							<span class="block label">Help</span>
						</a>
						<a href="/messages">
							<img src="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-64.png" srcset="https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-32.png 1x, https://slack.global.ssl.fastly.net/0dc1/img/icons/ios-64.png 2x" />
							<span class="block label">Launch</span>
						</a>
					</div>
								                    <ul id="header_team_nav">
			                        			                            <li class="active">
			                            	<a href="https://rdcep-summer.slack.com/home" target="https://rdcep-summer.slack.com/">
			                            					                            			<i class="ts_icon ts_icon_check_circle_o active_icon"></i>
			                            					                            					                            			<i class="team_icon default" style="background: #544538;">R</i>
			                            					                            		<span class="switcher_label team_name">rdcep-summer</span>
			                            	</a>
			                            </li>
			                        			                        <li id="add_team_option"><a href="https://slack.com/signin" target="_blank"><i class="ts_icon ts_icon_plus team_icon"></i> <span class="switcher_label">Sign in to another team...</span></a></li>
			                    </ul>
			                				</div>
			
			
		</header>
	
	<div id="page" >

		<div id="page_contents" >

<p class="print_only">
	<strong>Created by bglick on July 1, 2015 at 1:47 PM</strong><br />
	<span class="subtle_silver break_word">https://rdcep-summer.slack.com/files/bglick/F073J3BSL/florencenplotter.py</span>
</p>

<div class="file_header_container no_print"></div>

<div class="alert_container">
		<div class="file_public_link_shared alert" style="display: none;">
		
	<i class="ts_icon ts_icon_link"></i> Public Link: <a class="file_public_link" href="https://slack-files.com/T06BZ0F60-F073J3BSL-46e3166297" target="new">https://slack-files.com/T06BZ0F60-F073J3BSL-46e3166297</a>
</div></div>

<div id="file_page" class="card top_padding">

	<p class="small subtle_silver no_print meta">
		2KB Python snippet created on <span class="date">July 1st 2015</span>.
				<span class="file_share_list"></span>
	</p>

	<a id="file_action_cog" class="action_cog action_cog_snippet float_right no_print">
		<span>Actions </span><i class="ts_icon ts_icon_cog"></i>
	</a>
	<a id="snippet_expand_toggle" class="float_right no_print">
		<i class="ts_icon ts_icon_expand "></i>
		<i class="ts_icon ts_icon_compress hidden"></i>
	</a>

	<div class="large_bottom_margin clearfix">
		<pre id="file_contents">__author__ = &#039;Ben&#039;
&quot;&quot;&quot;This file, when run, will create a bar plot of the FlorenceN data&quot;&quot;&quot;
#The Python Plotting module is named plt for this file, so I can use it more easliy
import matplotlib.pyplot as plt
#Numpy (Numerical Python)
import numpy as np
#the CSV module is used to read data from csv files
import csv
#Collections.defaultdict is used for storing data into dictionaries
from collections import defaultdict

#Save the location of the file I am going to be reading from
location=&quot;C:\\Users\Ben\Desktop\FlorenceN.csv&quot;
#Creates an empty list to  store the data with
columns=defaultdict(list)
#Sets the file containing data to be local variable f
with open(location) as f:
        #sets up a dictionary reader that reads from file f
        reader=csv.DictReader(f)
        #accesses each element in the list reader
        for row in reader:
            #Accesses each sub-element in the list that is an element of the list reader
            for (k,v) in row.items():
                    #Appends each datum to the empty dictionary we created earlier
                    columns[k].append(v)
#Prints columns in order to make sure the data are correct
print(columns)
#creates a list of all th death counts
ZymoticD=[int(i) for i in columns[&#039;Zymotic diseases_y&#039;]]
#Sets the width of each column in the bar chart to be .5 inches
width=.5
#creates a range of values that will be used as the y list
n=np.arange(len(ZymoticD))
#creates the bar chart
p1=plt.bar(n, ZymoticD, color=&#039;r&#039;)
#labels the y axis
plt.ylabel(&#039;Deaths&#039;)
#labels the x axis
plt.xlabel(&#039;Date(1 bar represents 1 week)&#039;)
#labels the title
plt.title(&#039;Deaths(per week) due to Zymotic Diseases&#039;)
#Plots the x Axis
xAxis = columns[&#039;X&#039;]
#Adds scale on y axis
plt.yticks(np.arange(0,3000,500))
#Adds scale on x axis
plt.xticks(np.arange(0,24,5), (columns[&#039;X&#039;]))
#shows plot
plt.show()</pre>

		<p class="file_page_meta no_print" style="line-height: 1.5rem;">
			<label class="checkbox normal mini float_right no_top_padding no_min_width">
				<input type="checkbox" id="file_preview_wrap_cb"> wrap long lines
			</label>
		</p>

	</div>

	<div id="comments_holder" class="clearfix clear_both">
	<div class="col span_1_of_6"></div>
	<div class="col span_4_of_6 no_right_padding">
		<div id="file_page_comments">
			<div class="loading_hash_animation">
	<img src="https://slack.global.ssl.fastly.net/f85a/img/loading_hash_animation_@2x.gif" srcset="https://slack.global.ssl.fastly.net/272a/img/loading_hash_animation.gif 1x, https://slack.global.ssl.fastly.net/f85a/img/loading_hash_animation_@2x.gif 2x" alt="Loading" class="loading_hash" /><br />loading...
	<noscript>
		You must enable javascript in order to use Slack :(
				<style type="text/css">div.loading_hash { display: none; }</style>
	</noscript>
</div>		</div>	
		<form action="https://rdcep-summer.slack.com/files/bglick/F073J3BSL/florencenplotter.py" 
		id="file_comment_form" 
					class="comment_form"
				method="post">
			<a href="/team/ncdanica" class="member_preview_link" data-member-id="U07034TR9" >
			<span class="member_image thumb_36" style="background-image: url('https://secure.gravatar.com/avatar/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-72.png')" data-thumb-size="36" data-member-id="U07034TR9"></span>
		</a>		
		<input type="hidden" name="addcomment" value="1" />
	<input type="hidden" name="crumb" value="s-1435784600-58981d0498-☃" />

	<textarea id="file_comment" data-el-id-to-keep-in-view="file_comment_submit_btn" class="comment_input small_bottom_margin" name="comment" wrap="virtual" ></textarea>
	<span class="input_note float_left cloud_silver file_comment_tip">cmd+enter to submit</span>	<button id="file_comment_submit_btn" type="submit" class="btn float_right  ladda-button" data-style="expand-right"><span class="ladda-label">Add Comment</span></button>
</form>

<form
		id="file_edit_comment_form" 
					class="edit_comment_form hidden"
				method="post">
		<textarea id="file_edit_comment" class="comment_input small_bottom_margin" name="comment" wrap="virtual"></textarea><br>
	<span class="input_note float_left cloud_silver file_comment_tip">cmd+enter to submit</span>	<input type="submit" class="save btn float_right " value="Save Changes" />
	<button class="cancel btn btn_outline float_right small_right_margin ">Cancel</button>
</form>	
	</div>
	<div class="col span_1_of_6"></div>
</div>
</div>

	

		
	</div>
	<div id="overlay"></div>
</div>





<script type="text/javascript">
var cdn_url = 'https://slack.global.ssl.fastly.net';
</script>
			<script type="text/javascript">
<!--
	// common boot_data
	var boot_data = {
		start_ms: new Date().getTime(),
		app: 'web',
		is_mobile: false,
		user_id: 'U07034TR9',
		version_ts: '1435783475',
		version_uid: '5d62333be5c79b01b3ed343ad8a67cf1d526a47c',
		redir_domain: 'slack-redir.net',
		signin_url: 'https://slack.com/signin',
		abs_root_url: 'https://slack.com/',
		api_url: '/api/',
		team_url: 'https://rdcep-summer.slack.com/',
		image_proxy_url: 'https://slack-imgs.com/',
		api_token: 'xoxs-6407015204-7003163859-7100195440-8388346cc2',

		feature_status: false,
		feature_search_attachments: false,
		feature_archive_viewer: true,
		
		notification_sounds: [{"value":"b2.mp3","label":"Ding","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/b2.mp3"},{"value":"animal_stick.mp3","label":"Boing","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/animal_stick.mp3"},{"value":"been_tree.mp3","label":"Drop","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/been_tree.mp3"},{"value":"complete_quest_requirement.mp3","label":"Ta-da","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/complete_quest_requirement.mp3"},{"value":"confirm_delivery.mp3","label":"Plink","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/confirm_delivery.mp3"},{"value":"flitterbug.mp3","label":"Wow","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/flitterbug.mp3"},{"value":"here_you_go_lighter.mp3","label":"Here you go","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/here_you_go_lighter.mp3"},{"value":"hi_flowers_hit.mp3","label":"Hi","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/hi_flowers_hit.mp3"},{"value":"item_pickup.mp3","label":"Yoink","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/item_pickup.mp3"},{"value":"knock_brush.mp3","label":"Knock Brush","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/knock_brush.mp3"},{"value":"save_and_checkout.mp3","label":"Woah!","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/save_and_checkout.mp3"},{"value":"none","label":"None (sound off)"}],
		alert_sounds: [{"value":"frog.mp3","label":"Frog","url":"https:\/\/slack.global.ssl.fastly.net\/a34a\/sounds\/frog.mp3"}],
		call_sounds: [{"value":"gong.mp3","label":"Gong","url":"https:\/\/slack.global.ssl.fastly.net\/ec58\/sounds\/gong.mp3"}],

		feature_new_signup_flow: true,
		feature_at_here: false,
		feature_mpim_client: false,
		feature_admin_forced_sso_reset: false,
		feature_varietypack_optin: false,
		feature_reactions: false,
		feature_in_app_invites: true,
		feature_fullscreen_modals: true,
		feature_help_case_feedback: false,
		feature_spaces: false,
		feature_a11y_keyboard_shortcuts: false,
		feature_email_integration: false,
		feature_email_ingestion: false,
		feature_attachments_inline: false,
		feature_cmd_autocomplete: true,
		feature_ms_on_space: true,
		feature_flexpane_rework: true,
		feature_fix_files: false,
		feature_chat_sounds: false,
		feature_require_at: true,
		feature_image_proxy: true,
		feature_channel_eventlog_client: true,
		feature_bot_users: true,
		feature_muting: true,
		feature_macssb1_banner: true,
		feature_winssb1_banner: true,
		feature_latest_event_ts: true,
		feature_no_redirects_in_ssb: true,
		feature_referer_policy: true,
		feature_client_exif_orientation_on_uploads: true,
		feature_at_channel_warning: true,
		feature_at_channel_warning_non_admin_message: true,
		feature_pins: true,
		feature_join_leave_rollups: true,
		feature_bot_message_label: true,
		feature_oldest_msg_storing: true,
		feature_new_btns_in_channel_list: true,
		feature_box_plugin: true,
		feature_post_previews: false,
		feature_pricing_page_refresh: true,
		feature_client_date_formatting: false,
		feature_more_field_in_message_attachments: false,
		feature_user_hidden_msgs: false,
		feature_prompt_to_share: false,
		feature_file_url_private_conversion: false,
		feature_spaces_in_windows: false,
		feature_screenhero: false,
		feature_msg_input_revisions: true,
		feature_lazy_load_pins: true,
		feature_simple_latest: true,
		feature_channel_page_toggle_refactor: true,
		feature_custom_fields: false,
		feature_integrations_message_preview: false,
		feature_client_integration_management: false,
		feature_slash_commands_settings: false,
		feature_lite_to_free: true,
		feature_spaces_api_migration: false,
		feature_spaces_new_xp: false,
		feature_bot_profile: false,
		feature_two_factor_via_sms: false,
		feature_ssb_downloads: false,
		feature_omnibox_smart_spaces: false,
		feature_private_channels: false,
		feature_dropbox_plugin: false,

		img: {
			app_icon: 'https://slack.global.ssl.fastly.net/272a/img/slack_growl_icon.png'
		},
		page_needs_custom_emoji: false
	};



	// client boot data
			boot_data.login_data = JSON.parse('{\"ok\":true,\"self\":{\"id\":\"U07034TR9\",\"name\":\"ncdanica\",\"prefs\":{\"highlight_words\":\"\",\"user_colors\":\"\",\"color_names_in_list\":true,\"growls_enabled\":true,\"tz\":null,\"push_dm_alert\":true,\"push_mention_alert\":true,\"push_everything\":true,\"push_idle_wait\":2,\"push_sound\":\"b2.mp3\",\"push_loud_channels\":\"\",\"push_mention_channels\":\"\",\"push_loud_channels_set\":\"\",\"email_alerts\":\"none\",\"email_alerts_sleep_until\":0,\"email_misc\":true,\"email_weekly\":true,\"welcome_message_hidden\":false,\"all_channels_loud\":false,\"loud_channels\":\"\",\"never_channels\":\"\",\"loud_channels_set\":\"\",\"show_member_presence\":true,\"search_sort\":\"timestamp\",\"expand_inline_imgs\":true,\"expand_internal_inline_imgs\":true,\"expand_snippets\":false,\"posts_formatting_guide\":true,\"seen_welcome_2\":false,\"seen_ssb_prompt\":false,\"seen_spaces_new_xp_tooltip\":false,\"spaces_new_xp_banner_dismissed\":false,\"search_only_my_channels\":false,\"emoji_mode\":\"default\",\"emoji_use\":\"{\\\"heart\\\":1,\\\"simple_smile\\\":2,\\\"stuck_out_tongue\\\":1}\",\"has_invited\":false,\"has_uploaded\":false,\"has_created_channel\":false,\"search_exclude_channels\":\"\",\"messages_theme\":\"default\",\"webapp_spellcheck\":true,\"no_joined_overlays\":false,\"no_created_overlays\":false,\"dropbox_enabled\":false,\"seen_user_menu_tip_card\":false,\"seen_team_menu_tip_card\":false,\"seen_channel_menu_tip_card\":false,\"seen_message_input_tip_card\":false,\"seen_channels_tip_card\":false,\"seen_domain_invite_reminder\":false,\"seen_member_invite_reminder\":false,\"seen_flexpane_tip_card\":false,\"seen_search_input_tip_card\":false,\"mute_sounds\":false,\"arrow_history\":false,\"tab_ui_return_selects\":true,\"obey_inline_img_limit\":true,\"new_msg_snd\":\"knock_brush.mp3\",\"collapsible\":false,\"collapsible_by_click\":true,\"require_at\":true,\"ssb_space_window\":\"\",\"mac_ssb_bounce\":\"\",\"mac_ssb_bullet\":true,\"expand_non_media_attachments\":true,\"show_typing\":true,\"pagekeys_handled\":true,\"last_snippet_type\":\"\",\"display_real_names_override\":0,\"time24\":false,\"enter_is_special_in_tbt\":false,\"graphic_emoticons\":false,\"convert_emoticons\":true,\"autoplay_chat_sounds\":true,\"ss_emojis\":true,\"sidebar_behavior\":\"\",\"seen_onboarding_start\":true,\"onboarding_cancelled\":true,\"seen_onboarding_slackbot_conversation\":true,\"seen_onboarding_channels\":true,\"seen_onboarding_direct_messages\":true,\"seen_onboarding_invites\":false,\"seen_onboarding_search\":false,\"seen_onboarding_recent_mentions\":false,\"seen_onboarding_starred_items\":false,\"seen_onboarding_private_groups\":false,\"onboarding_slackbot_conversation_step\":10,\"mark_msgs_read_immediately\":true,\"start_scroll_at_oldest\":true,\"snippet_editor_wrap_long_lines\":false,\"ls_disabled\":false,\"sidebar_theme\":\"chocolate_theme\",\"sidebar_theme_custom_values\":\"{\\\"column_bg\\\":\\\"#544538\\\",\\\"menu_bg\\\":\\\"#42362B\\\",\\\"active_item\\\":\\\"#5DB09D\\\",\\\"active_item_text\\\":\\\"#FFFFFF\\\",\\\"hover_item\\\":\\\"#4A3C30\\\",\\\"text_color\\\":\\\"#FFFFFF\\\",\\\"active_presence\\\":\\\"#FFFFFF\\\",\\\"badge\\\":\\\"#5DB09D\\\"}\",\"f_key_search\":false,\"k_key_omnibox\":true,\"speak_growls\":false,\"mac_speak_voice\":\"com.apple.speech.synthesis.voice.Alex\",\"mac_speak_speed\":250,\"comma_key_prefs\":false,\"at_channel_suppressed_channels\":\"\",\"push_at_channel_suppressed_channels\":\"\",\"prompted_for_email_disabling\":false,\"full_text_extracts\":false,\"no_text_in_notifications\":false,\"muted_channels\":\"\",\"no_macssb1_banner\":false,\"no_winssb1_banner\":true,\"privacy_policy_seen\":true,\"search_exclude_bots\":false,\"fuzzy_matching\":false,\"load_lato_2\":false,\"fuller_timestamps\":false,\"last_seen_at_channel_warning\":0,\"enable_flexpane_rework\":false,\"flex_resize_window\":false,\"msg_preview\":false,\"msg_preview_displaces\":true,\"msg_preview_persistent\":true,\"emoji_autocomplete_big\":false,\"winssb_run_from_tray\":true,\"two_factor_auth_enabled\":false,\"two_factor_type\":null,\"mentions_exclude_at_channels\":true,\"confirm_clear_all_unreads\":true,\"confirm_user_marked_away\":true,\"box_enabled\":false,\"seen_single_emoji_msg\":false,\"confirm_sh_call_start\":true},\"created\":1435604669},\"team\":{\"id\":\"T06BZ0F60\",\"name\":\"rdcep-summer\",\"email_domain\":\"uchicago.edu\",\"domain\":\"rdcep-summer\",\"msg_edit_window_mins\":-1,\"prefs\":{\"default_channels\":[\"C06BYT4EL\",\"C06BZ0FCL\"],\"msg_edit_window_mins\":-1,\"allow_message_deletion\":true,\"hide_referers\":true,\"display_real_names\":false,\"who_can_at_everyone\":\"regular\",\"who_can_at_channel\":\"ra\",\"warn_before_at_channel\":\"always\",\"who_can_create_channels\":\"regular\",\"who_can_archive_channels\":\"regular\",\"who_can_create_groups\":\"ra\",\"who_can_post_general\":\"ra\",\"who_can_kick_channels\":\"admin\",\"who_can_kick_groups\":\"regular\",\"retention_type\":0,\"retention_duration\":0,\"group_retention_type\":0,\"group_retention_duration\":0,\"dm_retention_type\":0,\"dm_retention_duration\":0,\"file_retention_type\":0,\"file_retention_duration\":0,\"require_at_for_mention\":0,\"compliance_export_start\":0,\"auth_mode\":\"normal\"},\"icon\":{\"image_34\":\"https:\\/\\/slack.global.ssl.fastly.net\\/b3b7\\/img\\/avatars-teams\\/ava_0003-34.png\",\"image_44\":\"https:\\/\\/slack.global.ssl.fastly.net\\/b3b7\\/img\\/avatars-teams\\/ava_0003-44.png\",\"image_68\":\"https:\\/\\/slack.global.ssl.fastly.net\\/b3b7\\/img\\/avatars-teams\\/ava_0003-68.png\",\"image_88\":\"https:\\/\\/slack.global.ssl.fastly.net\\/b3b7\\/img\\/avatars-teams\\/ava_0003-88.png\",\"image_102\":\"https:\\/\\/slack.global.ssl.fastly.net\\/b3b7\\/img\\/avatars-teams\\/ava_0003-102.png\",\"image_132\":\"https:\\/\\/slack.global.ssl.fastly.net\\/b3b7\\/img\\/avatars-teams\\/ava_0003-132.png\",\"image_default\":true},\"over_storage_limit\":false,\"plan\":\"\"},\"latest_event_ts\":\"1435784000.000000\",\"channels\":[{\"id\":\"C06FN2ZCY\",\"name\":\"atlas\",\"is_channel\":true,\"created\":1434572166,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06FN3SQG\",\"name\":\"cco\",\"is_channel\":true,\"created\":1434572180,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06FMU7RU\",\"name\":\"citydata\",\"is_channel\":true,\"created\":1434572062,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06H20613\",\"name\":\"climate-emulator\",\"is_channel\":true,\"created\":1434649492,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06HFP82C\",\"name\":\"corn\",\"is_channel\":true,\"created\":1434666762,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06FN7H1B\",\"name\":\"datalibrary\",\"is_channel\":true,\"created\":1434572199,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06H1U9NE\",\"name\":\"energydemos\",\"is_channel\":true,\"created\":1434649516,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06HG141M\",\"name\":\"epa\",\"is_channel\":true,\"created\":1434667159,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06BYT4EL\",\"name\":\"general\",\"is_channel\":true,\"created\":1434387814,\"creator\":\"U06BZ03FF\",\"is_archived\":false,\"is_general\":true,\"has_pins\":false,\"is_member\":true,\"members\":[\"U06BZ03FF\",\"U06BZ7JR5\",\"U06C0AK44\",\"U06DT5HMW\",\"U06DT8RU7\",\"U06H1RXMF\",\"U06H1VDNE\",\"U06H2HQ48\",\"U06H72XSQ\",\"U06HEVC9M\",\"U06HFPVNW\",\"U06HPA43B\",\"U06JL9B63\",\"U06KA9UP4\",\"U06M9BL0P\",\"U06MZUAAD\",\"U06VBGAVD\",\"U06VBPTDZ\",\"U07034R3N\",\"U07034TR9\",\"U0703JXJS\",\"U0703K3NX\"],\"topic\":{\"value\":\"Company-wide announcements and work-based matters\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"This channel is for team-wide communication and announcements. All team members are in this channel.\",\"creator\":\"\",\"last_set\":0}},{\"id\":\"C0705MU84\",\"name\":\"hs-summer-scholars\",\"is_channel\":true,\"created\":1435607984,\"creator\":\"U06BZ03FF\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U06BZ03FF\",\"U06DT5HMW\",\"U06DT8RU7\",\"U06H2HQ48\",\"U06M9BL0P\",\"U06MZUAAD\",\"U06VBGAVD\",\"U06VBPTDZ\",\"U07034R3N\",\"U07034TR9\",\"U0703JXJS\",\"U0703K3NX\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"Announcements and such\",\"creator\":\"U06BZ03FF\",\"last_set\":1435607984}},{\"id\":\"C073G24TE\",\"name\":\"not-suspicious\",\"is_channel\":true,\"created\":1435780515,\"creator\":\"U0703JXJS\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U06H1VDNE\",\"U06M9BL0P\",\"U06VBGAVD\",\"U06VBPTDZ\",\"U07034R3N\",\"U07034TR9\",\"U0703JXJS\",\"U0703K3NX\"],\"topic\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"\",\"creator\":\"\",\"last_set\":0}},{\"id\":\"C06H1U19D\",\"name\":\"pyfund\",\"is_channel\":true,\"created\":1434649505,\"creator\":\"U06DT5HMW\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":false},{\"id\":\"C06BZ0FCL\",\"name\":\"random\",\"is_channel\":true,\"created\":1434387814,\"creator\":\"U06BZ03FF\",\"is_archived\":false,\"is_general\":false,\"has_pins\":false,\"is_member\":true,\"members\":[\"U06BZ03FF\",\"U06BZ7JR5\",\"U06C0AK44\",\"U06DT5HMW\",\"U06DT8RU7\",\"U06H1RXMF\",\"U06H1VDNE\",\"U06H2HQ48\",\"U06H72XSQ\",\"U06HEVC9M\",\"U06HFPVNW\",\"U06HPA43B\",\"U06JL9B63\",\"U06KA9UP4\",\"U06M9BL0P\",\"U06MZUAAD\",\"U06VBGAVD\",\"U06VBPTDZ\",\"U07034R3N\",\"U07034TR9\",\"U0703JXJS\",\"U0703K3NX\"],\"topic\":{\"value\":\"Non-work banter and water cooler conversation\",\"creator\":\"\",\"last_set\":0},\"purpose\":{\"value\":\"A place for non-work-related flimflam, faffing, hodge-podge or jibber-jabber you\'d prefer to keep out of more focused work-related channels.\",\"creator\":\"\",\"last_set\":0}}],\"groups\":[],\"ims\":[{\"id\":\"D07033U4R\",\"is_im\":true,\"user\":\"USLACKBOT\",\"created\":1435604669,\"is_user_deleted\":false},{\"id\":\"D07033U57\",\"is_im\":true,\"user\":\"U06BZ03FF\",\"created\":1435604669,\"is_user_deleted\":false},{\"id\":\"D0702T3L7\",\"is_im\":true,\"user\":\"U06BZ7JR5\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D07033U5P\",\"is_im\":true,\"user\":\"U06DT5HMW\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D0703ASJH\",\"is_im\":true,\"user\":\"U06DT8RU7\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D07034TV1\",\"is_im\":true,\"user\":\"U06H1RXMF\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D0702PMMW\",\"is_im\":true,\"user\":\"U06H72XSQ\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D0702VD0A\",\"is_im\":true,\"user\":\"U06HEVC9M\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D07034U03\",\"is_im\":true,\"user\":\"U06HPA43B\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D07031UA0\",\"is_im\":true,\"user\":\"U06JL9B63\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D0703G05A\",\"is_im\":true,\"user\":\"U06M9BL0P\",\"created\":1435605251,\"is_user_deleted\":false},{\"id\":\"D0702PMNC\",\"is_im\":true,\"user\":\"U06MZUAAD\",\"created\":1435604670,\"is_user_deleted\":false},{\"id\":\"D072YV5L7\",\"is_im\":true,\"user\":\"U06VBGAVD\",\"created\":1435761862,\"is_user_deleted\":false},{\"id\":\"D07032VD0\",\"is_im\":true,\"user\":\"U07034R3N\",\"created\":1435604773,\"is_user_deleted\":false},{\"id\":\"D0708Q0TX\",\"is_im\":true,\"user\":\"U0703JXJS\",\"created\":1435611260,\"is_user_deleted\":false},{\"id\":\"D0703J7TK\",\"is_im\":true,\"user\":\"U0703K3NX\",\"created\":1435605306,\"is_user_deleted\":false}],\"users\":[{\"id\":\"U0703K3NX\",\"name\":\"abisolaolawale\",\"deleted\":false,\"status\":null,\"color\":\"53b759\",\"real_name\":\"Abisola Olawale\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"Abisola\",\"last_name\":\"Olawale\",\"title\":\"\",\"skype\":\"\",\"phone\":\"\",\"real_name\":\"Abisola Olawale\",\"real_name_normalized\":\"Abisola Olawale\",\"email\":\"abbyh.olawale@yahoo.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/99e877572758e9286e8674ed82405e4a.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0024-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/99e877572758e9286e8674ed82405e4a.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0024-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/99e877572758e9286e8674ed82405e4a.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0024-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/99e877572758e9286e8674ed82405e4a.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0024-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/99e877572758e9286e8674ed82405e4a.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0024.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06DT5HMW\",\"name\":\"alison\",\"deleted\":false,\"status\":null,\"color\":\"3c989f\",\"real_name\":\"Alison Brizius\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Alison\",\"last_name\":\"Brizius\",\"skype\":\"alison.brizius\",\"real_name\":\"Alison Brizius\",\"real_name_normalized\":\"Alison Brizius\",\"email\":\"abrizius@uchicago.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3db9574fa570804a88f7524f5c40a70d.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3db9574fa570804a88f7524f5c40a70d.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3db9574fa570804a88f7524f5c40a70d.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3db9574fa570804a88f7524f5c40a70d.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3db9574fa570804a88f7524f5c40a70d.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013.png\"},\"is_admin\":true,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06C0AK44\",\"name\":\"annablinderman\",\"deleted\":false,\"status\":null,\"color\":\"e7392d\",\"real_name\":\"Anna Blinderman\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Anna\",\"last_name\":\"Blinderman\",\"title\":\"\",\"skype\":\"\",\"phone\":\"\",\"real_name\":\"Anna Blinderman\",\"real_name_normalized\":\"Anna Blinderman\",\"email\":\"anna.b.blinderman@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/23a78c7ac028c7a27e44882665d80618.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/23a78c7ac028c7a27e44882665d80618.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/23a78c7ac028c7a27e44882665d80618.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/23a78c7ac028c7a27e44882665d80618.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/23a78c7ac028c7a27e44882665d80618.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U07034R3N\",\"name\":\"aroitman\",\"deleted\":false,\"status\":null,\"color\":\"9e3997\",\"real_name\":\"Aroitman Roitman\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"Aroitman\",\"last_name\":\"Roitman\",\"real_name\":\"Aroitman Roitman\",\"real_name_normalized\":\"Aroitman Roitman\",\"email\":\"aroitman@cps.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/de08913795ef2098a6fe4e58ef488e97.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/de08913795ef2098a6fe4e58ef488e97.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/de08913795ef2098a6fe4e58ef488e97.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/de08913795ef2098a6fe4e58ef488e97.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/de08913795ef2098a6fe4e58ef488e97.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0015.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06MZUAAD\",\"name\":\"bglick\",\"deleted\":false,\"status\":null,\"color\":\"bb86b7\",\"real_name\":\"Benjamin Glick\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Benjamin\",\"last_name\":\"Glick\",\"real_name\":\"Benjamin Glick\",\"real_name_normalized\":\"Benjamin Glick\",\"email\":\"benjamin.h.glick@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1e754e5e038dd66fb0b8429c97b0e1b3.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0019-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1e754e5e038dd66fb0b8429c97b0e1b3.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0019-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1e754e5e038dd66fb0b8429c97b0e1b3.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0019-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1e754e5e038dd66fb0b8429c97b0e1b3.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0019-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/1e754e5e038dd66fb0b8429c97b0e1b3.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0019.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06M9BL0P\",\"name\":\"denise\",\"deleted\":false,\"status\":null,\"color\":\"d58247\",\"real_name\":\"\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"hdenise244@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/315274027317e33b6f20f3e26731c9c0.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0012-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/315274027317e33b6f20f3e26731c9c0.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0012-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/315274027317e33b6f20f3e26731c9c0.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0012-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/315274027317e33b6f20f3e26731c9c0.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0012-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/315274027317e33b6f20f3e26731c9c0.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0012.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06H1RXMF\",\"name\":\"fgregg\",\"deleted\":false,\"status\":null,\"color\":\"e96699\",\"real_name\":\"Forest Gregg\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Forest\",\"last_name\":\"Gregg\",\"real_name\":\"Forest Gregg\",\"real_name_normalized\":\"Forest Gregg\",\"email\":\"fgregg@datamade.us\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e0b6c74a03be663be1aa0a637980bb99.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e0b6c74a03be663be1aa0a637980bb99.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e0b6c74a03be663be1aa0a637980bb99.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e0b6c74a03be663be1aa0a637980bb99.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e0b6c74a03be663be1aa0a637980bb99.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06BZ7JR5\",\"name\":\"gueringerjohn\",\"deleted\":false,\"status\":null,\"color\":\"4bbe2e\",\"real_name\":\"John Gueringer\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"John\",\"last_name\":\"Gueringer\",\"real_name\":\"John Gueringer\",\"real_name_normalized\":\"John Gueringer\",\"email\":\"gueringerjohn@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a48d7720c1be6b6ca0bd5131c05e51e1.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0004-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a48d7720c1be6b6ca0bd5131c05e51e1.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0004-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a48d7720c1be6b6ca0bd5131c05e51e1.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0004-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a48d7720c1be6b6ca0bd5131c05e51e1.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0004-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/a48d7720c1be6b6ca0bd5131c05e51e1.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0004.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U0703JXJS\",\"name\":\"gustavotovar\",\"deleted\":false,\"status\":null,\"color\":\"c386df\",\"real_name\":\"Gustavo Tovar 3 14\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Gustavo Tovar 3\",\"last_name\":\"14\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-29\\/7007497893_4e0f9eaf744557864840_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-29\\/7007497893_4e0f9eaf744557864840_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-29\\/7007497893_4e0f9eaf744557864840_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-29\\/7007497893_4e0f9eaf744557864840_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-29\\/7007497893_4e0f9eaf744557864840_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-29\\/7007497893_4e0f9eaf744557864840_original.jpg\",\"real_name\":\"Gustavo Tovar 3 14\",\"real_name_normalized\":\"Gustavo Tovar 3 14\",\"email\":\"gustavo.tovar.3.14@gmail.com\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06HFPVNW\",\"name\":\"jelliott\",\"deleted\":false,\"status\":null,\"color\":\"99a949\",\"real_name\":\"\",\"tz\":\"America\\/Indiana\\/Indianapolis\",\"tz_label\":\"Eastern Daylight Time\",\"tz_offset\":-14400,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"jelliott@ci.uchicago.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/724c550db20922d4c77776b953539bad.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/724c550db20922d4c77776b953539bad.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0023-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/724c550db20922d4c77776b953539bad.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0023-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/724c550db20922d4c77776b953539bad.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/724c550db20922d4c77776b953539bad.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06KA9UP4\",\"name\":\"jr_jr_var_var\",\"deleted\":false,\"status\":null,\"color\":\"9b3b45\",\"real_name\":\"Juan Vera\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Juan\",\"last_name\":\"Vera\",\"phone\":\"815-878-2852\",\"real_name\":\"Juan Vera\",\"real_name_normalized\":\"Juan Vera\",\"email\":\"juegodiego.jv@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fb44922d40862a4086901763eb5e6476.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fb44922d40862a4086901763eb5e6476.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fb44922d40862a4086901763eb5e6476.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fb44922d40862a4086901763eb5e6476.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/fb44922d40862a4086901763eb5e6476.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0013.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06JL9B63\",\"name\":\"kylechard\",\"deleted\":false,\"status\":null,\"color\":\"4cc091\",\"real_name\":\"\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"chard@uchicago.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/655d7e6a8b312a4195289225ae5a9cf0.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/655d7e6a8b312a4195289225ae5a9cf0.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/655d7e6a8b312a4195289225ae5a9cf0.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/655d7e6a8b312a4195289225ae5a9cf0.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/655d7e6a8b312a4195289225ae5a9cf0.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0011.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06VBGAVD\",\"name\":\"mwpearsall\",\"deleted\":false,\"status\":null,\"color\":\"5a4592\",\"real_name\":\"Mwpearsall23\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"Mwpearsall23\",\"real_name\":\"Mwpearsall23\",\"real_name_normalized\":\"Mwpearsall23\",\"email\":\"mwpearsall23@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/c68985c8144e220b7b64e5074ec3bd72.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/c68985c8144e220b7b64e5074ec3bd72.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/c68985c8144e220b7b64e5074ec3bd72.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/c68985c8144e220b7b64e5074ec3bd72.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/c68985c8144e220b7b64e5074ec3bd72.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U07034TR9\",\"name\":\"ncdanica\",\"deleted\":false,\"status\":null,\"color\":\"235e5b\",\"real_name\":\"Danica Jayco\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"Danica\",\"last_name\":\"Jayco\",\"title\":\"\",\"skype\":\"\",\"phone\":\"\",\"real_name\":\"Danica Jayco\",\"real_name_normalized\":\"Danica Jayco\",\"email\":\"ncdanica@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0023-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0023-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/feb9a6dbd5fb2072de539e13a3a6813e.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0023.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06BZ03FF\",\"name\":\"radha\",\"deleted\":false,\"status\":null,\"color\":\"9f69e7\",\"real_name\":\"\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"real_name\":\"\",\"real_name_normalized\":\"\",\"email\":\"radar@uchicago.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/5d473e0b3bab47e87755654ab8ff3635.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/5d473e0b3bab47e87755654ab8ff3635.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/5d473e0b3bab47e87755654ab8ff3635.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/5d473e0b3bab47e87755654ab8ff3635.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/5d473e0b3bab47e87755654ab8ff3635.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0015.png\"},\"is_admin\":true,\"is_owner\":true,\"is_primary_owner\":true,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06H72XSQ\",\"name\":\"rblourenco\",\"deleted\":false,\"status\":null,\"color\":\"5b89d5\",\"real_name\":\"Ricardo Barros Lourenco\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Ricardo\",\"last_name\":\"Barros Lourenco\",\"image_24\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-18\\/6586121058_90d4c1c4436d0d41a524_24.jpg\",\"image_32\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-18\\/6586121058_90d4c1c4436d0d41a524_32.jpg\",\"image_48\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-18\\/6586121058_90d4c1c4436d0d41a524_48.jpg\",\"image_72\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-18\\/6586121058_90d4c1c4436d0d41a524_72.jpg\",\"image_192\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-18\\/6586121058_90d4c1c4436d0d41a524_192.jpg\",\"image_original\":\"https:\\/\\/s3-us-west-2.amazonaws.com\\/slack-files2\\/avatars\\/2015-06-18\\/6586121058_90d4c1c4436d0d41a524_original.jpg\",\"skype\":\"ricardobarroslourenco\",\"phone\":\"(773)744-5676\",\"title\":\"Research Assistant\",\"real_name\":\"Ricardo Barros Lourenco\",\"real_name_normalized\":\"Ricardo Barros Lourenco\",\"email\":\"rlourenc@mail.depaul.edu\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06DT8RU7\",\"name\":\"seth\",\"deleted\":false,\"status\":null,\"color\":\"674b1b\",\"real_name\":\"Seth Severns\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Seth\",\"last_name\":\"Severns\",\"real_name\":\"Seth Severns\",\"real_name_normalized\":\"Seth Severns\",\"email\":\"severns@uchicago.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e5b0169d137603fec1c6b715b8be32e9.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e5b0169d137603fec1c6b715b8be32e9.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e5b0169d137603fec1c6b715b8be32e9.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e5b0169d137603fec1c6b715b8be32e9.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e5b0169d137603fec1c6b715b8be32e9.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0014.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06HPA43B\",\"name\":\"skpurdue\",\"deleted\":false,\"status\":null,\"color\":\"df3dc0\",\"real_name\":\"Sydney Purdue\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Sydney\",\"last_name\":\"Purdue\",\"real_name\":\"Sydney Purdue\",\"real_name_normalized\":\"Sydney Purdue\",\"email\":\"skpurdue@uchicago.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3ba4628fe2ed116f1d4c84c6af51c2a8.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3ba4628fe2ed116f1d4c84c6af51c2a8.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3ba4628fe2ed116f1d4c84c6af51c2a8.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3ba4628fe2ed116f1d4c84c6af51c2a8.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/3ba4628fe2ed116f1d4c84c6af51c2a8.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0025.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06VBPTDZ\",\"name\":\"sllam\",\"deleted\":false,\"status\":null,\"color\":\"db3150\",\"real_name\":\"Stacylam9 lam\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"Stacylam9\",\"last_name\":\"lam\",\"real_name\":\"Stacylam9 lam\",\"real_name_normalized\":\"Stacylam9 lam\",\"email\":\"stacylam9@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/00399ed7dddd4821ec8fb9cebfd88007.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/00399ed7dddd4821ec8fb9cebfd88007.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/00399ed7dddd4821ec8fb9cebfd88007.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/00399ed7dddd4821ec8fb9cebfd88007.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0015-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/00399ed7dddd4821ec8fb9cebfd88007.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0015.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06H1VDNE\",\"name\":\"solorzano\",\"deleted\":false,\"status\":null,\"color\":\"e0a729\",\"real_name\":\"Chris Solorzano\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Chris\",\"last_name\":\"Solorzano\",\"title\":\"Graphic\\/Web Designer\",\"real_name\":\"Chris Solorzano\",\"real_name_normalized\":\"Chris Solorzano\",\"email\":\"solochris14@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e09fd50165f62ce3046120ad18f1097b.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e09fd50165f62ce3046120ad18f1097b.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e09fd50165f62ce3046120ad18f1097b.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e09fd50165f62ce3046120ad18f1097b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/e09fd50165f62ce3046120ad18f1097b.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0006.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06H2HQ48\",\"name\":\"tranv94\",\"deleted\":false,\"status\":null,\"color\":\"684b6c\",\"real_name\":\"Vinh Tran\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Vinh\",\"last_name\":\"Tran\",\"title\":\"\",\"skype\":\"\",\"phone\":\"\",\"real_name\":\"Vinh Tran\",\"real_name_normalized\":\"Vinh Tran\",\"email\":\"vtran2@luc.edu\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/86067b61e9a1532bbea7a00857ee6e0b.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/86067b61e9a1532bbea7a00857ee6e0b.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/86067b61e9a1532bbea7a00857ee6e0b.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/86067b61e9a1532bbea7a00857ee6e0b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/86067b61e9a1532bbea7a00857ee6e0b.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0017.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"U06HEVC9M\",\"name\":\"xin\",\"deleted\":false,\"status\":null,\"color\":\"2b6836\",\"real_name\":\"Xin Zhao\",\"tz\":\"America\\/Chicago\",\"tz_label\":\"Central Daylight Time\",\"tz_offset\":-18000,\"profile\":{\"first_name\":\"Xin\",\"last_name\":\"Zhao\",\"title\":\"\",\"skype\":\"\",\"phone\":\"7657145867\",\"real_name\":\"Xin Zhao\",\"real_name_normalized\":\"Xin Zhao\",\"email\":\"1220xin@gmail.com\",\"image_24\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2dfa2f4176d91b8fd8597632ce49d25b.jpg?s=24&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002-24.png\",\"image_32\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2dfa2f4176d91b8fd8597632ce49d25b.jpg?s=32&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002-32.png\",\"image_48\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2dfa2f4176d91b8fd8597632ce49d25b.jpg?s=48&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F272a%2Fimg%2Favatars%2Fava_0002-48.png\",\"image_72\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2dfa2f4176d91b8fd8597632ce49d25b.jpg?s=72&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002-72.png\",\"image_192\":\"https:\\/\\/secure.gravatar.com\\/avatar\\/2dfa2f4176d91b8fd8597632ce49d25b.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F3654%2Fimg%2Favatars%2Fava_0002.png\"},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false},{\"id\":\"USLACKBOT\",\"name\":\"slackbot\",\"deleted\":false,\"status\":null,\"color\":\"757575\",\"real_name\":\"slackbot\",\"tz\":null,\"tz_label\":\"Pacific Daylight Time\",\"tz_offset\":-25200,\"profile\":{\"first_name\":\"slackbot\",\"last_name\":\"\",\"image_24\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_24.png\",\"image_32\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_32.png\",\"image_48\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_48.png\",\"image_72\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_72.png\",\"image_192\":\"https:\\/\\/slack-assets2.s3-us-west-2.amazonaws.com\\/10068\\/img\\/slackbot_192.png\",\"real_name\":\"slackbot\",\"real_name_normalized\":\"slackbot\",\"email\":null},\"is_admin\":false,\"is_owner\":false,\"is_primary_owner\":false,\"is_restricted\":false,\"is_ultra_restricted\":false,\"is_bot\":false}],\"svn_rev\":\"dev\",\"min_svn_rev\":99999,\"version_ts\":1435783475,\"min_version_ts\":1435081219,\"cache_version\":\"v8-dog\",\"bots\":[{\"id\":\"B00\",\"name\":\"\",\"deleted\":false},{\"id\":\"B06LSNRN3\",\"name\":\"giphy\",\"deleted\":false,\"icons\":{\"image_48\":\"https:\\/\\/slack.global.ssl.fastly.net\\/0a04\\/plugins\\/giphy\\/assets\\/bot_48.png\"}}]}');
	
//-->
</script>			
			
					<!-- output_js "core" -->
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/421b/js/rollup-core_required.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/c212/js/libs/bootstrap_plastic.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/4bdd/js/libs/fastclick.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/8556/js/libs/headroom.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/c15e/js/plastic.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/4be5c/js/libs/bluebird-2.9.30-plus-electron-fix.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/eb1b/js/TS.web.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/5ca8c/js/analytics.js" crossorigin="anonymous"></script>

			<!-- output_js "secondary" -->
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/30fb/js/rollup-secondary_required.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/23e6e/js/TS.storage.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/9045/js/TS.ui.fs_modal.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/0b47/js/TS.ui.admin_invites.js" crossorigin="anonymous"></script>

		<!-- output_js "regular" -->
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/fdb7/js/TS.web.comments.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/b8c0/js/TS.web.file.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/002c/js/libs/codemirror.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://slack.global.ssl.fastly.net/9e78/js/codemirror_load.js" crossorigin="anonymous"></script>

		<script type="text/javascript">
	<!--
		boot_data.page_needs_custom_emoji = true;
		
		boot_data.file = JSON.parse('{\"id\":\"F073J3BSL\",\"created\":1435783623,\"timestamp\":1435783623,\"name\":\"FlorenceNPlotter.py\",\"title\":\"FlorenceNPlotter.py\",\"mimetype\":\"text\\/plain\",\"filetype\":\"python\",\"pretty_type\":\"Python\",\"user\":\"U06MZUAAD\",\"editable\":true,\"size\":1897,\"mode\":\"snippet\",\"is_external\":false,\"external_type\":\"\",\"is_public\":true,\"public_url_shared\":false,\"url\":\"https:\\/\\/slack-files.com\\/files-pub\\/T06BZ0F60-F073J3BSL-46e3166297\\/florencenplotter.py\",\"url_download\":\"https:\\/\\/slack-files.com\\/files-pub\\/T06BZ0F60-F073J3BSL-46e3166297\\/download\\/florencenplotter.py\",\"url_private\":\"https:\\/\\/files.slack.com\\/files-pri\\/T06BZ0F60-F073J3BSL\\/florencenplotter.py\",\"url_private_download\":\"https:\\/\\/files.slack.com\\/files-pri\\/T06BZ0F60-F073J3BSL\\/download\\/florencenplotter.py\",\"permalink\":\"https:\\/\\/rdcep-summer.slack.com\\/files\\/bglick\\/F073J3BSL\\/florencenplotter.py\",\"permalink_public\":\"https:\\/\\/slack-files.com\\/T06BZ0F60-F073J3BSL-46e3166297\",\"edit_link\":\"https:\\/\\/rdcep-summer.slack.com\\/files\\/bglick\\/F073J3BSL\\/florencenplotter.py\\/edit\",\"preview\":\"__author__ = \'Ben\'\\n\\\"\\\"\\\"This file, when run, will create a bar plot of the FlorenceN data\\\"\\\"\\\"\\n#The Python Plotting module is named plt for this file, so I can use it more easliy\\nimport matplotlib.pyplot as plt\\n#Numpy (Numerical Python)\\nimport numpy as np\\n#the CSV module is used to read data from csv files\\nimport csv\\n#Collections.defaultdict is used for storing data into dictionaries\\nfrom collections import defaultdict\",\"preview_highlight\":\"<div class=\\\"sssh-code\\\"><div class=\\\"sssh-line\\\"><pre>__author__ <span>=<\\/span> <span class=\\\"sssh-string\\\">\'Ben\'<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-string\\\">&quot;&quot;&quot;This file, when run, will create a bar plot of the FlorenceN data&quot;&quot;&quot;<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-comment\\\">#The Python Plotting module is named plt for this file, so I can use it more easliy<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-keyword\\\">import<\\/span> matplotlib.<span class=\\\"sssh-property\\\">pyplot<\\/span> <span class=\\\"sssh-keyword\\\">as<\\/span> plt<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-comment\\\">#Numpy (Numerical Python)<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-keyword\\\">import<\\/span> numpy <span class=\\\"sssh-keyword\\\">as<\\/span> np<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-comment\\\">#the CSV module is used to read data from csv files<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-keyword\\\">import<\\/span> <span class=\\\"sssh-keyword\\\">csv<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-comment\\\">#Collections.defaultdict is used for storing data into dictionaries<\\/span><\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><span class=\\\"sssh-keyword\\\">from<\\/span> <span class=\\\"sssh-keyword\\\">collections<\\/span> <span class=\\\"sssh-keyword\\\">import<\\/span> defaultdict<\\/pre><\\/div>\\n<div class=\\\"sssh-line\\\"><pre><\\/pre><\\/div>\\n<\\/div>\",\"lines\":49,\"lines_more\":39,\"channels\":[\"C0705MU84\"],\"groups\":[],\"ims\":[],\"comments_count\":1,\"initial_comment\":{\"id\":\"Fc073JLNFM\",\"created\":1435783624,\"timestamp\":1435783624,\"user\":\"U06MZUAAD\",\"comment\":\"This is an annotated version of the file that was posted in github.  There are comments above every line that explain what the following line is doing.\"}}');
		boot_data.file.comments = JSON.parse('[{\"id\":\"Fc073JLNFM\",\"created\":1435783624,\"timestamp\":1435783624,\"user\":\"U06MZUAAD\",\"comment\":\"This is an annotated version of the file that was posted in github.  There are comments above every line that explain what the following line is doing.\"}]');

		

		var g_editor;

		$(function(){

			var wrap_long_lines = !!TS.model.code_wrap_long_lines;

			g_editor = CodeMirror(function(elt){
				var content = document.getElementById("file_contents");
				content.parentNode.replaceChild(elt, content);
			}, {
				value: $('#file_contents').text(),
				lineNumbers: true,
				matchBrackets: true,
				indentUnit: 4,
				indentWithTabs: true,
				enterMode: "keep",
				tabMode: "shift",
				viewportMargin: Infinity,
				readOnly: true,
				lineWrapping: wrap_long_lines
			});

			$('#file_preview_wrap_cb').bind('change', function(e) {
				TS.model.code_wrap_long_lines = $(this).prop('checked');
				g_editor.setOption('lineWrapping', TS.model.code_wrap_long_lines);
			})

			$('#file_preview_wrap_cb').prop('checked', wrap_long_lines);

			CodeMirror.switchSlackMode(g_editor, 'python');
		});

		
		$('#file_comment').css('overflow', 'hidden').autogrow();
	//-->
	</script>

			<script type="text/javascript">TS.boot(boot_data);</script>
	<!-- slack-www221 / 2015-07-01 14:03:20 / v5d62333be5c79b01b3ed343ad8a67cf1d526a47c -->

</body>
</html>