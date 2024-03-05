<script lang="ts">
  import ContentList from "$lib/utils/contents";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";
  import Navitagion from "$lib/components/Navitagion.svelte";
  import { fade, fly, scale, slide } from "svelte/transition";
  import Tooltip from "$lib/components/Tooltip.svelte";
  import { onMount } from "svelte";
  import { direction, pageIdx } from "$lib/utils/nav.store";

  // let $pageIdx = 0;

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

  $: nextPage = findNext($pageIdx);
  $: prevPage = findPrev($pageIdx);

  let navOpen = true;
  // let direction = 1;
  let initFocus = false;

  onMount(() => {
    setTimeout(() => {
      navOpen = false;

      initFocus = true;
      setTimeout(() => {
        initFocus = false;
      }, 2000);
    }, 1200);
  });
</script>

<div class="flex flex-col items-center mb-12">
  <button on:click={() => goto("../")} class="w-full relative">
    <img
      src="../title.jpg"
      id="banner"
      class="w-full h-20 lg:object-cover lg:object-top"
      alt=""
    />
    <div
      class="absolute top-0 w-full lg:flex md:flex hidden items-center justify-center h-full text-5xl text-white font-semibold"
    >
      <div
        class="border-b-2 border-b-transparent hover:border-b-white transition-all duration-500"
      >
        Union Zindabad
      </div>
    </div>
  </button>

  <main
    class="relative flex lg:flex-row md:flex-row flex-col justify-between pt-12 lg:px-20 md:px-20 gap-10 transition-all ease-in-out duration-200"
  >
    <button
      class="absolute lg:left-4 md:left-4 lg:top-auto lg:w-fit top-2 w-full flex items-center justify-center transition-all ease-in-out duration-200"
      on:click={() => {
        navOpen = !navOpen;
      }}
    >
      <span class="lg:hidden md:hidden font-semibold text-lg">Contents</span>
      <Tooltip bind:focus={initFocus} text={navOpen ? "Close" : "Navigation"}>
        <span
          class="fa fa-angle-double-left hover:bg-gray-200 p-3 rounded-full transition-all ease-in-out duration-200"
          class:rotate-180={navOpen}
        ></span>
      </Tooltip>
    </button>

    {#if navOpen}
      <div class="hidden lg:flex md:flex whitespace-nowrap relative z-[100]">
        <Navitagion current={$page.params.id} />
      </div>

      <div class="lg:hidden md:hidden whitespace-nowrap relative z-[100]">
        <Navitagion mobile current={$page.params.id} />
      </div>
    {/if}

    {#key $pageIdx}
      <div
        in:fly={{ x: 500 * $direction, duration: 500 }}
        id="site-content"
        class="text-lg font-serif text-left flex flex-col items-center transition-all ease-in-out duration-200 lg:max-w-[50vw] md:max-w-[50vw] max-w-[90vw]"
      >
        <div class="w-full flex justify-between">
          {#if prevPage !== null}
            <button
              class="group"
              on:click={() => {
                $direction = -1;
                goto(`../${prevPage}`, { noScroll: true });
              }}
            >
              <span
                class="fa fa-arrow-left group-hover:-translate-x-2 transition-all ease-in-out duration-300"
              ></span>
              Prev
            </button>
          {:else}
            <div />
          {/if}

          {#if nextPage !== null}
            <button
              hidden={nextPage === null}
              class="group"
              on:click={() => {
                $direction = 1;
                goto(`../${nextPage}`, { noScroll: true });
              }}
            >
              Next
              <span
                class="fa fa-arrow-right group-hover:translate-x-2 transition-all ease-in-out duration-300"
              ></span>
            </button>
          {:else}
            <div />
          {/if}
        </div>

        <slot />
      </div>
    {/key}
  </main>
</div>

<style type="postcss">
  :global(h2.entry-title) {
    @apply text-5xl text-center py-4 border-b-2 mb-4 px-10;
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
    @apply flex items-center flex-col py-8 lg:max-w-[50vw] md:max-w-[50vw];
  }

  :global(.site-content figcaption) {
    @apply text-center text-sm pt-2;
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

  #banner {
  }
</style>
