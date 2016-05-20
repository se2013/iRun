// 点击收藏按钮，实现收藏功能

$(document).ready(function() {
	collect();
});

function collect() {
	$('button.collect').click(function() {
		var plan_id = $(this).val();
		var account = $('span.account').text();
		$.ajax({
	   		type: "POST",  
	   		url: "/manage/otherPlan", 
	   		data: {'plan_id':plan_id, 'account':account},
	   		success: function() {
	   			//提示成功
	   			 $(this).removeAttr("disabled");
	   		},
	   		error: function() {
	   		}
		});
	});
}

// 将本地浏览器存储的cookie填入用户名input框
function fillUserNameInBlank() {
	var username = $.cookie('username');
	if (!username)
		return;
	$('input#username').val(username);
}

// 将用户名input框的内容设置为cookie
function getUserNameFormBlank() {
	$('input#submit_JS').click(function() {
		var username = $('input#username').val();
		if (username != '') {
			$.cookie('username', null);
			$.cookie('username', username, { expires: 1460 });
		}
			
		return true;
	});
	return true;
}