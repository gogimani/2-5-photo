function openModal(src) {
    var modal = document.getElementById('modal');
    var modalImg = document.getElementById('modalImg');
    modal.style.display = "block";
    modalImg.src = src;
}

function closeModal() {
    var modal = document.getElementById('modal');
    modal.style.display = "none";
}
