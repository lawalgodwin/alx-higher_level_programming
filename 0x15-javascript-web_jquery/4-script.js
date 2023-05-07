$(document).ready(function () {
  function toggleColor () {
    const currentState = $('header').css('color');
    if (currentState === 'rgb(255, 0, 0)') {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else if (currentState === 'rgb(0, 255, 0)') {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
    console.log($('header').css('color'));
  }
  $('DIV#toggle_header').bind('click', function () {
    toggleColor();
  });
});
