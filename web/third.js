function mySubmitFunction(e) {
    let form = document.form3
    if(form.username.value == "") {
        alert("Please complete username.")
        form.username.focus();
        e.preventDefault();
        return
    }

    if(form.password.value == "") {
        alert("Please complete password.")
        form.password.focus();
        e.preventDefault();
        return
    }

    if (form.password.value != form.password.value.toUpperCase()) {
        alert("Your password contains lower case letter.")
        form.password.focus();
        e.preventDefault();
        return
    }
}