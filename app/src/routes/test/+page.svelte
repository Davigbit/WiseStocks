<!-- <script>
    import { onMount } from 'svelte';
    let data = [];
  
    async function fetchData() {
      const response = await fetch('../api/data.js');
      data = await response.json();
    }
  
    onMount(fetchData);
  </script>


<div>
    <h1>Random Numbers from Python</h1>
  
    {#if data.length > 0}
      <ul>
        {#each data as number}
          <li>{number}</li>
        {/each}
      </ul>
    {:else}
      <p>Loading...</p>
    {/if}
</div> -->
  
<!-- 
<script>
  import EmbeddedGraph from "$lib/components/EmbeddedGraph old.svelte";
  
</script>
  
<div>
  <EmbeddedGraph/>
</div> -->