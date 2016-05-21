// 点击收藏按钮，实现收藏功能

$(document).ready(function() {
	delete_plan();
});

function delete_plan() {
	$('button.deletePlan').click(function() {
		var plan_id = $(this).val();
		$.ajax({
	   		type: "POST",  
	   		url: "/maintainplan", 
	   		data: {'plan_id':plan_id},
	   		success: function() {
	   			//提示成功
	   			 location.reload() 
	   		},
	   		error: function() {
	   		}
		});
	});
}

