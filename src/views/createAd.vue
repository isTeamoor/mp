<template>
    <div class="newForm">
        <h1>Create new Ad</h1>
        <button @click="query">Query server</button>
        <div>
            <h3>Server response:</h3>
            <p>{{ serverResponse }}</p>
        </div>
        <p>Input Label</p><input type="text" id="new label" name="new label"><br>
        <p>Input Text Content</p><textarea name="new textContent" rows="10" cols="30"></textarea><br>

    </div>
</template>
<script>
export default {
    name: 'createAd',
    data() {
        return {
            serverResponse: ''
        }
    },
    methods: {
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
</style>