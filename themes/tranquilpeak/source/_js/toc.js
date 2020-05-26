(function($) {
    $(document).ready(function() {
        $( 'ol .toc-child' ).contents().unwrap().wrap( '<ul></ul>' );
    });

})(jQuery);