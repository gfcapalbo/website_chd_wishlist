$(document).ready(function () {

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