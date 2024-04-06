<script>
  import StockBox from "$lib/components/StockBox.svelte"
</script>

<div>
    <h1 class="text-center mb-5 title">Trade Stocks!</h1>
    <p class="m-3 text-center description-text"> Use our <strong>AI model</strong> to get the <strong>best predictions</strong> about the future and do the right investments! </p>
    <div class="container">
        <div class="row row-cols-4">
            <div class="col"><StockBox company={"NA"}/></div>
            <div class="col"><StockBox company={"SU"} currentStock={"120 000"} currentProfit={123000}/></div>
            <div class="col"><StockBox company={"BCE"} currentStock={"120 000"} currentProfit={-300000000.5}/></div>
            <div class="col"><StockBox company={"IMO"}/></div>
        </div>
    </div>

</div>
<style>
    
    .description-text{
        font-size: 2em;
    }
    .col{
        padding: 1%;
        
    }
    
</style>

