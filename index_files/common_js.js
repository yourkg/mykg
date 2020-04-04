(function(){
	var location_href = location.href
	if (location_href.indexOf('moorelite.com') > -1) {
		document.getElementsByClassName('icp')[0].innerText = '苏ICP备15038517号-2'
	}
	wx.miniProgram.postMessage({ data:{title: document.title, desc:''} });
	
	jQuery('.miniprogramBtn').click(function () {
		var url = 'icdesign'
		if (['2632', '7130', '7224'].indexOf(pageId) > -1) {
			url = 'incubation'
		}else if (['1934'].indexOf(pageId) > -1) {
			url = 'icdesign'
		}else if (['1969', '3490', '2969', '3886'].indexOf(pageId) > -1) {
			url = 'supplychain'
		}else if (['1784', '3723', '3815', '3848', '3767', '3626', '1915'].indexOf(pageId) > -1) {
			url = 'talent'
		}
		wx.miniProgram.navigateTo({url: '/pages/jsjform/' + url + '/main?' + location.href.split('?')[1]})
	})
})()