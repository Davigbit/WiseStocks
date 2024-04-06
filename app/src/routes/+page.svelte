<script>


    function goToTrade(){
        window.location.href = "/trade-stocks";
    }
    // let data = {"NA": {"today_value": 113.76, "today_change": 0.2997707635337713}, "SU": {"today_value": 53.01, "today_change": 1.3769363166953508}, "BCE": {"today_value": 45.04, "today_change": -0.7054673721340394}, "IMO": {"today_value": 99.54, "today_change": 1.3232899022801419}}
</script>

<div>
    <div class="intro-msg">
        <h1 class="text-center">Welcome to Wise Stocks!</h1>
        <p class="text-center">The stock investor you need to make your money more lucrative...</p>
        <button class="d-grid mx-auto mt-5 btn btn-primary btn-lg" on:click={goToTrade}>Get Started!</button>
    </div>
    
</div>

<style>
    .intro-msg{
        margin-top: 15%;
    }
</style>


