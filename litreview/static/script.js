const input = document.querySelector('#id_image_0');
const preview = document.querySelector('.image-bck-img');

if (input !== null) {
    input.addEventListener('change', updateImageDisplay);
}

function updateImageDisplay() {
    let curFiles = []
    if (input !== null) {
        curFiles = input.files;
    }
    if (curFiles.length > 0) {
        const curFile = curFiles[0]
        preview.style.backgroundImage = `url(${URL.createObjectURL(curFile)})`;
        preview.style.border = 'none';
    } else {
        preview.style.border = '1px dotted grey';
        preview.style.backgroundImage = 'none';
    }
}