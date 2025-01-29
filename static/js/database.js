function showDashboard() {
    document.getElementById('dashboard').style.display = 'block';
    document.getElementById('user').style.display = 'none';
    document.getElementById('venue').style.display = 'none';
    document.getElementById('lesson').style.display = 'none';
    document.getElementById('appointment').style.display = 'none';
    document.getElementById('payment').style.display = 'none';
}

function showUser() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'block';
    document.getElementById('venue').style.display = 'none';
    document.getElementById('lesson').style.display = 'none';
    document.getElementById('appointment').style.display = 'none';
    document.getElementById('payment').style.display = 'none';
}

function showVenue() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('venue').style.display = 'block';
    document.getElementById('lesson').style.display = 'none';
    document.getElementById('appointment').style.display = 'none';
    document.getElementById('payment').style.display = 'none';
}

function showLesson() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('venue').style.display = 'none';
    document.getElementById('lesson').style.display = 'block';
    document.getElementById('appointment').style.display = 'none';
    document.getElementById('payment').style.display = 'none';
}

function showAppointment() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('venue').style.display = 'none';
    document.getElementById('lesson').style.display = 'none';
    document.getElementById('appointment').style.display = 'block';
    document.getElementById('payment').style.display = 'none';
}

function showSection(section) {
    document.querySelectorAll('.content-section').forEach(function(sec) {
    sec.style.display = 'none';
    });
    document.getElementById(section).style.display = 'block';
}

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const section = urlParams.get('section');
    if (section) {
        showSection(section);
    } else {
        showSection('dashboard');
    }
};