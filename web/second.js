function isPerfect(n) {
    n = parseInt(n, 10);
    console.log(n)
    let sum = 1;
    for(let i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            if (i * i != n)
                sum = sum + i + n/i;
            else
                sum+=1;
        }
    }

    if (sum == n && n != 1)
        return true;
    return false;
}

function btnOnClick() {

    let e = document.getElementById("list");
    let strUser = e.options[e.selectedIndex].value;
    
    if (isPerfect(strUser)) {
        window.location.href = "D:\\workspace\\internet_engineering_projects\\web\\third.html"
    } else {
        alert("Please select a perfect number.")
    }
}
