document.addEventListener('DOMContentLoaded', () => {
    
    // Connect to websocket
    var socket = io(location.protocol + '//' + document.domain + ':' + location.port);
    
    socket.on('connect', function(){
        console.log('connected');
    });

    socket.on('crow added', function(data){
        console.log('crow added')
        document.querySelector('#crows_count').innerHTML = data.crows_count
    });

    socket.on('disconnect', function(){
        console.log('disconnected');
    });

    document.querySelector('#socket').onclick = () => {
        socket.emit('add crow');
    };
    

   document.querySelector('#ajax').onclick = () => {

        // Создаём объект AJAX запроса

        const request = new XMLHttpRequest();
        
        // Указываем метод запроса и адрес

        request.open('POST', '/add_crow');

        // Регистрируем функцию на выполнение запроса

        request.onload = () => {

            // Парсим данные из ответа

            const data = JSON.parse(request.responseText);

            // Записываем количество ворон в нужный тег

            document.querySelector('#crows_count').innerHTML = data.crows_count;
            
        };

        // Посылаем AJAX запрос

        request.send();
        
        // Возвращаем ложь, чтобы избежать срабатывания submit формы

        return false;
    };

});