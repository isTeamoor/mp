<template>
    <div class="adList">
        <h1>Ad List</h1>
        <button @click="showAllAds">Show All Ads</button>
        <div class="miniAds">
            <figure v-for="miniAd in  miniAds " :key="miniAd.id">
                <button @click="deleteAd(miniAd.id)">X</button>
                <h4>{{ miniAd.label }}</h4>
                <img :src="`http://127.0.0.1:8000/db/getImg/${miniAd.id}`" />

                <figcaption>{{ miniAd.textContent }}</figcaption>
            </figure>
        </div>
    </div>
</template>

<script>
export default {
    //<img :src="require(`../../src/assets/images/${miniAd.id}.jpg`)" :alt="miniAd.id" />
    name: 'adList',
    data() {
        return {
            miniAds: []
        }
    },
    methods: {
        deleteAd(id) {
            fetch('http://127.0.0.1:8000/db/deleteAd', {
                method: 'POST',
                headers: { "Content-type": "application/json; charset=UTF-8" },
                body: JSON.stringify({
                    id: id
                })
            }).then(d => d.json()).then(d => this.miniAds = d)
        },
        showAllAds() {
            fetch('http://127.0.0.1:8000/db/getAllAds').then(d => d.json()).then(d => this.miniAds = d)
        },
        getImg(id) {
            fetch(`http://127.0.0.1:8000/db/getImg/${id}`)
        }

    }
}
</script>
<style scoped>
.adList {
    width: 70%;
    height: 85vh;
    margin-left: auto;
    margin-right: auto;
    border: 2px solid black;
    background-color: azure;
}

.miniAds {
    display: flex;
    flex-wrap: wrap;
}

figure {
    width: 25%;
    height: 10%;
    border: 2px solid gray;
    text-align: center;
    position: relative;
}

figure button {
    left: 45%;
    top: 10px;
    background-color: red;
    position: relative;
}

h1 {
    text-align: center;
}
</style>