<script lang="ts">
  import ContentList from "$lib/utils/contents";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";
  import Navitagion from "$lib/components/Navitagion.svelte";
  import { fade, fly, scale, slide } from "svelte/transition";
  import Tooltip from "$lib/components/Tooltip.svelte";
  import { onMount } from "svelte";

  let pageIdx = 0;
  const findContent = (id: string) => {
    for (let i = 0; i < ContentList.length; i++) {
      if (ContentList[i].id === id) {
        pageIdx = i;
        return ContentList[i];
      }

      let chapters = ContentList[i].chapters;
      if (chapters) {
        for (let j = 0; j < chapters.length; j++) {
          if (chapters[j].id === id) {
            pageIdx = i + (j + 1) / 100;
            return chapters[j];
          }
        }
      }
    }

    goto("/404");
  };

  const findNext = (idx: number) => {
    if (idx < ContentList.length - 1) {
      if (idx > Math.floor(idx)) {
        let chapters = ContentList[Math.floor(idx)].chapters;
        if (!chapters) return ContentList[Math.floor(idx)].id;

        if (Number.parseInt(idx.toString().split(".")[1]) === chapters.length) {
          return ContentList[Math.floor(idx) + 1].id;
        }

        return chapters[Number.parseInt(idx.toString().split(".")[1])].id;
      }
      let nextChapters = ContentList[Math.floor(idx)].chapters;
      if (nextChapters) {
        return nextChapters[0].id;
      }

      return ContentList[Math.floor(idx) + 1].id;
    } else {
      return null;
    }
  };

  const findPrev = (idx: number) => {
    if (idx > 0) {
      if (idx > Math.floor(idx)) {
        let chapters = ContentList[Math.floor(idx)].chapters;
        if (!chapters) return ContentList[Math.floor(idx)].id;

        if (Number.parseInt(idx.toString().split(".")[1]) === 1) {
          return ContentList[Math.floor(idx)].id;
        }

        return chapters[Number.parseInt(idx.toString().split(".")[1]) - 2].id;
      }
      let prevChapters = ContentList[Math.floor(idx) - 1].chapters;
      if (prevChapters) {
        return prevChapters[prevChapters.length - 1].id;
      }

      return ContentList[Math.floor(idx) - 1].id;
    } else {
      return null;
    }
  };

  $: siteContent = findContent($page.params.id);
  $: nextPage = findNext(pageIdx);
  $: prevPage = findPrev(pageIdx);

  let navOpen = true;
  let direction = 1;
  let initFocus = false;

  onMount(() => {
    setTimeout(() => {
      navOpen = false;

      initFocus = true;
      setTimeout(() => {
        initFocus = false;
      }, 1200);
    }, 1200);
  });
</script>

<!-- <img src="../title.jpg" class="w-full h-40 object-cover" alt="" /> -->

<main
  class="relative flex justify-between pt-10 px-20 gap-10 transition-all ease-in-out duration-200"
>
  <button
    class="absolute left-4 transition-all ease-in-out duration-200"
    on:click={() => {
      navOpen = !navOpen;
    }}
  >
    <Tooltip bind:focus={initFocus} text={navOpen ? "Close" : "Navigation"}>
      <span
        class="fa fa-angle-double-left hover:bg-gray-200 p-3 rounded-full transition-all ease-in-out duration-200"
        class:rotate-180={navOpen}
      ></span>
    </Tooltip>
  </button>

  {#if navOpen}
    <div class="whitespace-nowrap relative z-[100]">
      <Navitagion current={$page.params.id} bind:direction />
    </div>
  {/if}

  {#key siteContent}
    <div
      in:fly={{ x: 500 * direction, duration: 500 }}
      id="site-content"
      class="text-lg font-serif text-left flex flex-col items-center transition-all ease-in-out duration-200 max-w-[50vw]"
    >
      <div class="w-full flex justify-between">
        <button on:click={() => goto(`../${prevPage}`, { noScroll: true })}>
          <span
            class="fa fa-arrow-left hover:scale-150 transition-all ease-in-out duration-300"
          ></span>
          Prev
          <!-- {prevPage} -->
        </button>
        <!-- {pageIdx} -->
        <button on:click={() => goto(`../${nextPage}`, { noScroll: true })}>
          <!-- {nextPage} -->
          Next
          <span
            class="fa fa-arrow-right hover:scale-150 transition-all ease-in-out duration-300"
          ></span>
        </button>
      </div>

      {@html siteContent?.content}
    </div>
  {/key}
</main>

<style type="postcss">
  :global(h2.entry-title) {
    @apply text-5xl text-center py-4 border-b-2 mb-4 px-10 whitespace-nowrap;
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

  :global(.site-content a) {
    @apply border-b border-b-black transition-all ease-in-out duration-200 hover:border-b-transparent;
  }
</style>
