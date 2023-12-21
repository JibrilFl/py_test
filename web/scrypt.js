window.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.btn').addEventListener('click',  async () => {

        const ip = document.querySelector('.hosts__input').value;
        const message = document.querySelector('.host__message');

        let hosts = await eel.host_down(ip)();

        if (hosts[1]) {
            message.innerHTML += `<span style="color: red;">${hosts[1]}</span></br>`;
        } else {
            if (hosts[0].length < 11) {
            message.innerHTML += '<span style="color: red;">Ошибка при добавлении портов</span></br>';
            const substr = hosts[0].match(/[^$\\n]+[$:]/g).join()
            message.innerHTML += `<span style="color: red;">${hosts[0].replace(substr, '')}</span></br>`;
            } else {
                message.innerHTML += '<span style="color: green;">Порты успешно добавлены</span></br>';
            }
        }

    });

    document.querySelector('#vnc').addEventListener('click',  async () => {
        const ip = document.querySelector('.hosts__input').value;
        const message = document.querySelector('.host__message');

        let vnc = await eel.vnc_down(ip)();

        if (vnc.length === 2) {
            if (vnc[0] === 0) {
                message.innerHTML += `<span style="color: green;">${vnc[1]}</span></br>`;
            } else {
                message.innerHTML += `<span style="color: red;">${vnc[1]}</span></br>`;
            }
        }
    });

    document.querySelector('#cry').addEventListener('click',  async () => {
        const ip = document.querySelector('.hosts__input').value;
        const message = document.querySelector('.host__message');

        let cry = await eel.crypto_down(ip)();

        if (cry.length === 2) {
            if (cry[0] === 0) {
                message.innerHTML += `<span style="color: green;">${cry[1]}</span></br>`;
            } else {
                message.innerHTML += `<span style="color: red;">${cry[1]}</span></br>`;
            }
        }
    });
});