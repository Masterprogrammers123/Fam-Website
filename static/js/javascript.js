console.warn("[RUNNING] App is starting [RUNNING]")

function checkForm() {
    console.log("Validating form...")
    var name = document.getElementsByName("Name")
    var email = document.getElementsByName("Email")
    var pass = document.getElementsByName("Password")
    var tosChecked = document.getElementsByName("tosChecked")
    console.log(name, email, pass, tosChecked)
    if (name.length < 100) {
        console.error("Name is longer then 100")
        var long_name = document.getElementsByName("invalid-feedback-name")
        long_name.innerHTML = "Are you sure this is your name? If so, please use a nickname for it to be under 100 chars")
    }
}
