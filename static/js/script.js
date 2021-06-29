
        $("input[name=holo]").change(function () {
            var max = 3;
            if ($("input[name=holo]:checked").length == max) {
                $("input[name=holo]").attr('disabled', 'disabled');
                $("input[name=holo]:checked").removeAttr('disabled');
            } else {
                $("input[name=holo]").removeAttr('disabled');
            }
        })

        function  search() {
            var fruit = '';

            var dd = '';
            var radio = document.getElementsByName("holo");
            for (var i = 0; i < radio.length; i++) {
                if (radio[i].checked == true) {
                    dd = radio[i].value;
                    fruit = fruit + "," + dd;
                }
            }

        }

