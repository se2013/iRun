// 点击收藏按钮，实现收藏功能

$(document).ready(function() {
	delete_user();
});

function delete_user() {
	$('button.deleteUser').click(function() {
		var user_account = $(this).val();
		$.ajax({
	   		type: "POST",  
	   		url: "/maintainuser", 
	   		data: {'user_account':user_account},
	   		success: function() {
	   			//提示成功
	   			 location.reload() 
	   		},
	   		error: function() {
	   		}
		});
	});
}

