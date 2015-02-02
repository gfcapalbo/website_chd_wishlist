$(document).ready(function () {


	$('.favorites_option').submit( function(){
		chosenform=this;
			var elements = document.querySelectorAll( 'feedback *' );
			$('<input />').attr('type', 'hidden')
         .attr('name', "summary")
         .attr('value', document.getElementById("feedback").innerHTML)
         .appendTo(chosenform);
         return true;
    });



    $('.addwish').each(function () {
        console.log(this);
        var addwish = this;
        $(addwish).on('click' , function ()
        {
            openerp.jsonRpc('/chd_init/wishadd/', 'call',
                 {
                 'toadd_id': my_chd_result,
                  }).then(function (data) {
                      var data_js = eval(data);
                      console.log("THIS IS THE DATA" + data_js);
                  })
        });
    });


});