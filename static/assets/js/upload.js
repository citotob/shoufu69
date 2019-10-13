$(document).on('submit', '#uploadForm',function(e){
    //e.preventDefault();

	var formData = new FormData($('uploadForm')[0]);
    $.ajax({
        xhr : function() {
            var xhr = new window.XMLHttpRequest();

            xhr.upload.addEventListener('progress', function(e) {
                if (e.lengthComputable) {
                    
                    console.log('Bytes Loaded: ' + e.loaded);
                    console.log('Total Size: ' + e.total);
                    console.log('Percentage Uploaded: ' + (e.loaded / e.total))

                    var percent = Math.round((e.loaded / e.total) * 100);

                    $('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
                }
            });

            return xhr;
        },
        type:'POST',
        url:'{% url "upload-video" %}',
        data : formData,
        processData : false,
        contentType : false,
        success : function() {
            alert('File uploaded!');
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        },        
    });
});