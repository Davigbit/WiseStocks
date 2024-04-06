<script>
    import {page} from '$app/stores'
    import EmbeddedGraph from "$lib/components/EmbeddedGraph.svelte";
    import Test from"$lib/components/Test.svelte"
    const company = $page.params.company;
</script>


<div>
    <h1 class="text-center pb-5 title">{company}</h1>

    <div class="container">
        <div class="row justify-content-center align-items-center">
            <!-- <div class="col text-center facts-container">
                
                <div class="info-box text-center mb-3 p-3">Improve: 50%</div>
                <div class="info-box text-center mb-3 p-3">Improve: 50%</div>
                
            </div> -->
            <div class="col  text-center"> <img src={`/graphs/${company}_last_30_days.png`} alt=""></div>
            <div class="col  text-center"> <img src={`/graphs/${company}_next_7_days.png`} alt=""></div>
        </div>
    </div>

    <!-- <EmbeddedGraph {company}/>
    <Test/> -->
</div>

<style>
    .info-box{
        background-color: white;
        color: black;
    }
    img{
        width: 100%;
        height: 100%;
    }
    .facts-container{
        height: 100%;
    }
</style>