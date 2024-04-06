<script>
    export let company = "Company"
    export let currentStock = "500 000";
    export let currentProfit = 212.5;

    function goToCompanyPage(){
        window.location.href = `trade-stocks/${company}`;
    }

    function int_to_str_formate(n){
        let s = n.toString();
        if (s.includes("-")){
            s = s.slice(1);
        }
        let final_string = "";
        if(s.includes('.')){
            let int_s = s.slice(0, s.indexOf(".")-1)
            let deci_s = s.slice(s.indexOf("."), s.indexOf(".")+3)
            final_string = back_space(int_s) + deci_s
        }else{
            final_string = back_space(s) + ".00";
        }

        return final_string;
    }

    function back_space(s){
        let final_string = "";
        for (let i = 0; i<s.length ; i++){
            final_string = s.charAt(s.length-1-i) + final_string;
            if ((s.length-1-i)%3 == 0){
                final_string = ' ' + final_string;
            }
        }
        return final_string;
    }

    let data = {"NA": {"today_value": 113.76, "today_change": 0.2997707635337713}, "SU": {"today_value": 53.01, "today_change": 1.3769363166953508}, "BCE": {"today_value": 45.04, "today_change": -0.7054673721340394}, "IMO": {"today_value": 99.54, "today_change": 1.3232899022801419}}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="box border">
<div class="p-3 container" on:click={goToCompanyPage} role="button" tabindex="0">
    <div class="row">
        <div class="col align-self-center">
            <h3 class="company-name pb-3">{company}</h3>
            <div class="pb-2 stock-state">{data[company]["today_value"]}</div>
            
        </div>
        <div class="col">
            <img src={`/logos/${company}.png`} alt="not found">
        </div>
        <div class="row">
            <div class="profit" class:loss={currentProfit<0}>{currentProfit>0 ? "+" : "-"}0{int_to_str_formate(data[company]["today_change"])}%</div>
        </div>
    </div>
    
</div>
<!-- <button on:click={() => int_to_str_formate(currentProfit)}> test</button> -->
</div>

<style>
    .box{
        background-color: rgb(235,225,192);
        width: 100%;
    }
    .company-name{
        color: rgb(16, 148, 169);
    }
    .stock-state{
        color: black;
        font-weight: bold;
    }
    .profit{
        color:green;
        font-weight: bold;
    }
    .loss{
        color:red;
        font-weight: bold;
    }

    .box:hover{
        background-color: rgb(230,133,51);
    }
    img{
        width: 100%;
       
    }
    
</style>