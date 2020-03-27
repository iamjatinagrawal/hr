$(document).ready(function() {
          $('#example').DataTable({

            "iDisplayLength": 25,
            "aLengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]]
            
            // "aLengthMenu":[[5, 10, 25, -1], [5, 10, 25, "All"]],
            //   "iDisplayLength": 10,
            //   "iDisplayStart":10
             } 
              );
      } );


function checkAll(bx) {
  var cbs = document.getElementsByTagName('input');
  for(var i=0; i < cbs.length; i++) {
    if(cbs[i].type == 'checkbox') {
      cbs[i].checked = bx.checked;
    }
  }
}