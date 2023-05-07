$(document).ready(function () {
  $('DIV#add_item').bind('click', function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });
});
