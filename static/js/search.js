let search = $('#id_search');
let url = 'http://localhost:9000/json-accounts/?search=';

let addAccount = function (account, container){
    let div = document.createElement('div');
    div.className = 'user_card'
    let div_about_user = document.createElement('div');
    div_about_user.className = 'about_user'
    let div_user_pic_div = document.createElement('div');
    div_user_pic_div.className = 'user_pic_div'
    let img = document.createElement('img');
    img.className = 'user_pic'
    let div_about_user_name = document.createElement('div');
    div_about_user_name.className = 'about_user_name'
    let div_about_user_scope = document.createElement('div');
    div_about_user_scope.className = 'about_user_scope'
    let about_user_name_heading = document.createElement('h4');
    about_user_name_heading.className = 'about_user_name_heading'
    let about_user_scope_heading = document.createElement('h5');
    about_user_scope_heading.className = 'about_user_scope_heading'

    let link = document.createElement('a');
    $(link).attr('href', `/accounts/${account.id}`);
    link.className = 'user_card_link'
    link.append(div_about_user)
    link.append(div_user_pic_div)

    div_about_user.append(div_about_user_name);
    div_about_user.append(div_about_user_scope);

    div_about_user_name.append(about_user_name_heading);
    let first_name = `${account.first_name}`;
    about_user_name_heading.append(first_name);
    about_user_name_heading.append(' ')
    let last_name = `${account.last_name}`;
    about_user_name_heading.append(last_name)

    let occupation = `${account.occupation}`;
    div_about_user_scope.append(about_user_scope_heading);
    about_user_scope_heading.append(occupation)
    if (account.avatar__image === null) {
        img.src = `/static/svg/user.png`;
        div_user_pic_div.append(img);
        img.alt = 'avatar image';
    } else {
        img.src = `/uploads/${account.avatar__image}`;
        div_user_pic_div.append(img);
        img.alt = 'avatar image';
    }
    div.append(link);
    container.append(div);
}
renderResult = function (accounts){
    let account_container = $('.block_profiles');
    account_container.empty();
    for(let account of accounts){
        addAccount(
            account,
            account_container
        );
    }
}
let getAccounts = function (){
    let value = search.val();
    $.ajax({
        url: url + value
    }).done(
        function (data){
            renderResult(data);
        }
    )
}
search.on('keyup', getAccounts);



