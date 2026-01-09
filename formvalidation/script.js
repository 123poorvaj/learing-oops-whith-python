let name = document.querySelector('#Name');
let mail = document.querySelector('#Mail');
let age = document.querySelector('#Age');
let occupation = document.getElementById("occupation");
let Hobbies = document.getElementById("Hobbies");
let message = document.getElementById('textarea');
let gender = document.mainform.gender;
let devices = document.mainform.devices;

function validation() {
    if (name.value == '') {
        alert("please enter your name")
        name.focus();
        return false;
    } else if (mail.value == '') {
        alert("please enter your MailID")
        mail.focus();
        return false;
    } else if (age.value == '') {
        alert("Enter your Age");
        age.focus();
        return false;
    } else if (occupation.value == 'choose an occupation') {
        alert("choose occupaion");
        return false;
        occupation.focus();
    } else if (Hobbies.value == 'choose an Hobbies') {
        alert("choose hobbise");
        Hobbies.focus();
        return false;

    } else if (message.value == '') {
        alert('Enter Your oppenion');
        message.focus();
        return false;
    }
    let devicecheck = false;
    for (let i = 0; i < devices.length; i++) {
        if (devices[i].checked) {
            devicecheck = true;
            break;
        }
    }
    if (!devicecheck) {
        alert("enter devices");
        devices[0].focus();
        return false;
    }
    let checkgender = false;
    for (i = 0; i < gender.length; i++) {
        if (gender[i].checked) {
            checkgender = true;
            break;
        }
    }
    if (!checkgender) {
        alert('enter gender');
        gender[0].focus();
        return false;
    }
    return true;
}