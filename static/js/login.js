"use strict"
let ask = (wants_account, yes, no) => {
    if (confirm(wants_account)) {
        // if the user does want the account, then I will collect their info
        yes();
    }
    else {
        no();
    }
}

let getInfo = () => {
    let name = prompt("Please enter your name", "John Doe");
};


ask("Do you want to create an account?", getInfo, "Ok Then!");