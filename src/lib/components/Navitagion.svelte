<script lang="ts">
  import contents from "$lib/utils/contents";
  import { goto } from "$app/navigation";
  import { linear } from "svelte/easing";
  import { slide } from "svelte/transition";

  export let current = "";

  const changePage = (id: string) => {
    goto(`../${id}`);
  };

  $: console.log(current);

</script>

<div transition:slide={{axis: "x"}} class="flex flex-col items-start">
  {#each contents as item}
    <button
      class:font-bold={current === item.id}
      on:click={() => changePage(item.id)}
    >
      {item.name}
    </button>

    {#if item.chapters}
      <div class="pl-8 flex flex-col items-start">
        {#each item.chapters as chapter}
          <button
            class:font-bold={current === chapter.id}
            on:click={() => changePage(chapter.id)}
          >
            {chapter.name}
          </button>
        {/each}
      </div>
    {/if}
  {/each}
</div>
