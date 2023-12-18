<template>
    <div class="newForm">
        <h1>Create new Ad</h1>

        <img class="imgPreview" />

        <form method="POST" action='http://127.0.0.1:8000/db/createNewAd' enctype="multipart/form-data">
            <label for="new label">Input new label</label>
            <input type="text" id="new label" name="label"><br>
            <label for="new textContent">Input new textContent</label>
            <textarea name="textContent" id="new textContent" rows="10" cols="30"></textarea><br>
            <label for="new img">Input new Img</label>
            <input type="file" name="img" id="new img" @change="showPreview" />
            <button type="submit">Submit</button>
        </form>

    </div>
</template>
<script>
export default {
    name: 'createAd',
    data() {
        return {
            serverResponse: '',
            photo: ''
        }
    },
    methods: {
        showPreview(event) {
            const imgBox = document.querySelector('.imgPreview');
            const file = event.target.files[0];
            imgBox.src = window.URL.createObjectURL(file);
        },




        query() {
            fetch('http://127.0.0.1:8000/db/createNewAd', {
                method: 'POST',
                headers: { "Content-type": "application/json; charset=UTF-8" },
                body: JSON.stringify({
                    label: document.querySelector('input[name="new label"]').value,
                    textContent: document.querySelector('textarea[name="new textContent"]').value
                })
            }).then(d => d.json()).then(d => {
                this.serverResponse = d;
                document.querySelector('input[name="new label"]').value = null;
                document.querySelector('textarea[name="new textContent"]').value = null
            })
        },
        getImage() {
            const imgPreview = document.querySelector('.imgPreview')
            document.querySelector('.imgPreview').setAttribute('src', 'http://127.0.0.1:8000/db/getImg/9') //fetch('http://127.0.0.1:8000/db/getImg').then(file => console.log(file))
        }
    }

}
</script>
<style scoped>
.newForm {
    width: 70%;
    height: 85vh;
    margin-left: auto;
    margin-right: auto;
    border: 2px solid black;
    background-color: azure;
}

h1 {
    text-align: center;
}

.imgPreview {
    width: 400px;
    height: 400px;
    float: right;
    border: 5px inset black;
    margin-right: 10px;
}

form label {
    display: inline-block;
    width: 200px;
    height: 50px;
}

form button {
    display: block;
    margin: auto;
}

form {
    display: inline-block;
    max-width: 50%;
}
</style>