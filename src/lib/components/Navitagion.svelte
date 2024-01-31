<script lang="ts">
  import contents from "$lib/utils/contents";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";

  export let current = '';

  const changePage = (id: string) => {
    goto(`../${id}`);
  };

  $: console.log(current);
  
</script>

<div class="flex flex-col items-start">
  {#each contents as item}
    <button
      class:font-bold={current === item.id}
      on:click={() => changePage(item.id)}
    >
      {item.name}
    </button>

    <div class="pl-8 flex flex-col items-start">
      {#if item.chapters}
        {#each item.chapters as chapter}
          <button
            class:font-bold={current === chapter.id}
            on:click={() => changePage(chapter.id)}
          >
            {chapter.name} 
          </button>
        {/each}
      {/if}
    </div>
  {/each}
</div>
