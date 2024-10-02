<script lang="ts">
  import ContentList from "$lib/utils/contents_";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";
  import Navitagion from "$lib/components/Navitagion.svelte";
  import { fade, fly, scale, slide } from "svelte/transition";
  import Tooltip from "$lib/components/Tooltip.svelte";
  import { onMount } from "svelte";
  import { direction, pageIdx } from "$lib/utils/nav.store";
  import NextPrevNav from "$lib/components/NextPrevNav.svelte";
  import { base } from "$app/paths";

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
    if ($page.params.id === "cover") goto("../");

    setTimeout(() => {
      navOpen = false;

      initFocus = true;
      setTimeout(() => {
        initFocus = false;
      }, 4000);
    }, 6000);
  });

  let scrollY: number;
</script>

<svelte:window bind:scrollY />

<div
  class="flex flex-col items-center mb-12 selection:bg-black selection:text-white"
>
  <button on:click={() => goto(`${base}/`)} class="w-full relative">
    <img
      src="{base}/title.jpg"
      id="banner"
      class="w-full h-20 lg:object-cover lg:object-top md:object-cover md:object-top"
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

  <!-- <div class="px-4 w-full"> -->
  <NextPrevNav {nextPage} {prevPage} />
  <!-- </div> -->

  <main
    class="relative flex lg:flex-row md:flex-row flex-col justify-between pt-12 lg:px-20 md:px-20 gap-10 transition-all ease-in-out duration-200"
  >
    <button
      class="absolute lg:left-4 md:left-4 lg:w-fit md:w-fit top-2 md:mt-8 md:pt-0.5 lg:mt-8 lg:pt-0.5 w-full flex items-center justify-center gap-0 transition-all ease-in-out duration-200"
      on:click={() => {
        navOpen = !navOpen;
      }}
    >
      <!-- w-3 break-words uppercase top-0 pt-10 -->
      <span
        class="absolute from-[#9b4d3a] text-white bg-gradient-to-l to-[#737f59] p-2 pr-9 rounded-t-lg lg:-rotate-90 md:-rotate-90 md:mt-24 lg:mt-24 uppercase"
        >Contents</span
      >
      <Tooltip bind:focus={initFocus} text={navOpen ? "Close" : "Navigation"}>
        <span
          class="fa fa-angle-double-left text-white p-3 translate-y-11 lg:translate-y-0 md:translate-y-0 rounded-full transition-all ease-in-out duration-200"
          class:rotate-180={navOpen}
        ></span>
      </Tooltip>
    </button>

    {#if navOpen}
      <div
        class="hidden lg:flex md:flex whitespace-nowrap relative z-[100] -ml-6 -mt-1 h-fit rounded-tl-none rounded-lg p-1 from-[#9b4d3a] bg-gradient-to-l to-[#737f59]"
      >
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
        class="text-lg text-left flex flex-col items-center transition-all ease-in-out duration-200 lg:max-w-[55vw] md:max-w-[55vw] max-w-[90vw]"
      >
        <slot />

        <div class="w-full pt-6">
          <NextPrevNav scrollOnNav full {nextPage} {prevPage} />
        </div>
      </div>
    {/key}

    {#if scrollY !== 0}
      <button
        transition:fade
        class="fixed right-6 bottom-6 z-[999] rounded-full object-cover bg-slate-100 py-0.5 group hover:-translate-y-1 transition-all duration-500"
        on:click={() => {
          window.scrollTo({ top: 0, behavior: "smooth" });
        }}
      >
        <span
          class="fa fa-angle-left rotate-90 py-4 px-5 group-hover:scale-110 transition-all duration-500"
        ></span>
      </button>
    {/if}
  </main>
</div>

<style type="postcss">
  :global(.site-content) {
    font-family: "brandon grotesque", sans-serif !important;
    @apply max-w-[90vw] mx-auto;
  }

  :global(.entry-content) {
    @apply max-w-[90vw] mx-auto;
  }

  :global(.site-content img) {
    @apply hover:-translate-y-2 hover:-translate-x-2 hover:rotate-1 transition-all ease-in-out duration-200;
  }

  :global(h2.entry-title) {
    @apply text-5xl text-center pb-6 px-10;
  }

  :global(.entry-content h2) {
    @apply text-2xl text-center;
  }

  :global(.site-content img) {
    @apply rounded-lg max-w-[90vw] lg:max-w-full md:max-w-full;
  }

  :global(.site-content, .entry-content) {
    @apply flex flex-col items-center font-serif;
  }

  :global(.site-content figure) {
    @apply flex items-center flex-col py-8 lg:max-w-[50vw] md:max-w-[50vw] max-w-[90vw] mx-auto;
  }

  :global(.site-content figcaption) {
    @apply text-center text-sm pt-2 break-words max-w-[90vw] mx-auto;
  }

  :global(.site-content li) {
    @apply pl-4 max-w-[90vw] mx-auto;
  }
  :global(.site-content p) {
    @apply py-3 max-w-[90vw] mx-auto;
  }

  :global(.site-content p iframe) {
    @apply max-w-[90vw] mx-auto;
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
