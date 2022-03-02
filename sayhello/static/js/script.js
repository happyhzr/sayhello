$(function () {
    function render_time() {
        return memont($(this).data('timestamp')).format('lll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        { title: render_time() }
    );
});