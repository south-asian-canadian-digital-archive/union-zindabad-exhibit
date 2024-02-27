<script lang="ts">
  import contents from "$lib/utils/contents";
  import { goto } from "$app/navigation";
  import { linear } from "svelte/easing";
  import { slide } from "svelte/transition";
  import { onMount } from "svelte";

  export let current = "";
  export let direction = 1;

  let expanded = {} as Record<string, boolean>;
  let lastIdx = 0;

  const changePage = (id: string, idx: number) => {
    if (idx > lastIdx) direction = 1;
    else if (idx < lastIdx) direction = -1;
    else direction = 0;

    lastIdx = idx;

    goto(`../${id}`);
  };

  onMount(() => {
    expanded = {};
    for (let i = 0; i < contents.length; i++) {
      if (contents[i].chapters) expanded[contents[i].id] = true;
    }
  });
</script>

<div
  transition:slide={{ axis: "x" }}
  class="flex flex-col gap-1 items-start w-full"
>
  {#each contents as item, idxi}
    <button
      class="hover:bg-gray-200 px-4 py-1 rounded transition-all ease-in-out duration-200 w-full text-left flex justify-between items-center"
      class:font-semibold={current === item.id}
      class:bg-gray-100={item.chapters}
      class:bg-gray-50={!item.chapters}
      on:click={() => changePage(item.id, idxi)}
    >
      {item.name}

      {#if item.chapters}
        <button
          on:click|stopPropagation={() => {
            expanded[item.id] = !expanded[item.id];
          }}
          class="fa fa-angle-right transition-all ease-in-out duration-300"
          class:rotate-90={expanded[item.id]}
        ></button>
      {/if}
    </button>

    {#if item.chapters && expanded[item.id]}
      <div
        transition:slide
        class="chapters flex flex-col gap-1 items-start w-full text-left"
      >
        {#each item.chapters as chapter, idxc}
          <button
            class="pl-14 hover:bg-gray-200 bg-gray-50 px-4 py-1 rounded transition-all ease-in-out duration-200 w-full text-left"
            class:font-bold={current === chapter.id}
            class:bg-gray-200={current === chapter.id}
            on:click={() => changePage(chapter.id, idxi + idxc / 100)}
          >
            {chapter.name}
          </button>
        {/each}
      </div>
    {/if}
  {/each}
</div>
