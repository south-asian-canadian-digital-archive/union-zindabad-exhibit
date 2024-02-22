<script lang="ts">
  import ContentList from "$lib/utils/contents";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";
  import Navitagion from "$lib/components/Navitagion.svelte";
  import { fade, fly, scale, slide } from "svelte/transition";
  import { linear } from "svelte/easing";
  import Tooltip from "$lib/components/Tooltip.svelte";

  const findContent = (id: string) => {
    for (let i = 0; i < ContentList.length; i++) {
      if (ContentList[i].id === id) {
        return ContentList[i];
      }

      let chapters = ContentList[i].chapters;
      if (chapters) {
        for (let j = 0; j < chapters.length; j++) {
          if (chapters[j].id === id) {
            return chapters[j];
          }
        }
      }
    }

    goto("/404");
  };

  $: siteContent = findContent($page.params.id);

  let navOpen = false;
</script>

<main
  class="relative flex justify-between pt-10 px-20 gap-10 transition-all ease-in-out duration-200"
>
  <button
    class="absolute left-4 transition-all ease-in-out duration-200"
    on:click={() => {
      navOpen = !navOpen;
    }}
  >
    <Tooltip text={navOpen ? "Close" : "Navigation"}>
      <span
        class="fa fa-angle-double-left hover:bg-gray-200 p-3 rounded-full transition-all ease-in-out duration-200"
        class:rotate-180={navOpen}
      ></span>
    </Tooltip>
  </button>

  {#if navOpen}
    <div class="whitespace-nowrap">
      <Navitagion current={$page.params.id} />
    </div>
  {/if}

  <div
    id="site-content"
    class="text-lg font-serif text-left flex justify-center transition-all ease-in-out duration-200 max-w-[50vw]"
  >
    {@html siteContent?.content}
  </div>
</main>

<style type="postcss">
  :global(h2.entry-title) {
    @apply text-3xl text-center py-4;
  }
</style>
