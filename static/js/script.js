
        $("input[name=checkbox_4]").change(function () {
            var max = 3;
            if ($("input[name=checkbox_4]:checked").length == max) {
                $("input[name=checkbox_4]").attr('disabled', 'disabled');
                $("input[name=checkbox_4]:checked").removeAttr('disabled');
            } else {
                $("input[name=checkbox_4]").removeAttr('disabled');
            }
        })
