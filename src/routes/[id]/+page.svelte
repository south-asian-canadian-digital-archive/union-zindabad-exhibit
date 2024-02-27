<script lang="ts">
  import ContentList from "$lib/utils/contents";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";
  import Navitagion from "$lib/components/Navitagion.svelte";
  import { fade, fly, slide } from "svelte/transition";
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

  let navOpen = true;
</script>

<main
  transition:slide={{ duration: 500 }}
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

  {#key siteContent}
    <div
      in:fade={{ duration: 500 }}
      id="site-content"
      class="text-lg font-serif text-left flex justify-center transition-all ease-in-out duration-200 max-w-[50vw]"
    >
      {@html siteContent?.content}
    </div>
  {/key}
</main>

<style type="postcss">
  :global(h2.entry-title) {
    @apply text-3xl text-center py-4 border-b-2 mb-4 px-4 whitespace-nowrap;
  }

  :global(.entry-content h2) {
    @apply text-2xl text-center;
  }

  :global(.site-content img) {
    @apply rounded-lg;
  }

  :global(.site-content) {
    @apply flex flex-col items-center;
  }

  :global(.site-content figure) {
    @apply flex items-center flex-col py-8 max-w-[50vw];
  }

  :global(.site-content figcaption) {
    @apply text-center text-sm;
  }

  :global(.site-content li) {
    @apply pl-4;
  }
  :global(.site-content p) {
    @apply py-3;
  }

  :global(.site-content img.aligncenter) {
    @apply mx-auto;
  }

  :global(.site-content blockquote) {
    @apply p-4 bg-gray-100 rounded-lg text-base;
  }

  :global(.site-content .alignleft) {
    @apply float-left mr-4;
  }

  :global(.site-content hr.before-footnotes) {
    @apply mt-8 mb-4;
  }

  :global(.site-content .footnotes > ol) {
    @apply list-decimal pl-4 text-base;
  }
</style>
