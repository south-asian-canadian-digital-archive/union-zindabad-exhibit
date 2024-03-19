<script lang="ts">
  import { goto } from "$app/navigation";
  import { direction } from "$lib/utils/nav.store";

  export let nextPage: string | null;
  export let prevPage: string | null;
  export let full = false;
  export let scrollOnNav = false;
</script>

<div class="w-full flex justify-between">
  {#if prevPage !== null}
    <button
      class="group from-[#9b4d3a] text-white bg-gradient-to-l to-[#737f59] p-2 px-4"
      class:rounded-lg={full}
      class:rounded-br-lg={!full}
      on:click={() => {
        $direction = -1;
        if (prevPage === "cover") goto("../");
        else goto(`../${prevPage}`, { noScroll: !scrollOnNav });
      }}
    >
      <span
        class="fa fa-arrow-left group-hover:-translate-x-2 transition-all ease-in-out duration-300"
      ></span>
      Last Page
    </button>
  {:else}
    <div />
  {/if}

  {#if nextPage !== null}
    <button
      hidden={nextPage === null}
      class="group from-[#9b4d3a] text-white bg-gradient-to-r to-[#737f59] p-2 px-4"
      class:rounded-lg={full}
      class:rounded-bl-lg={!full}
      on:click={() => {
        $direction = 1;
        goto(`../${nextPage}`, { noScroll: !scrollOnNav });
      }}
    >
      Next Page
      <span
        class="fa fa-arrow-right group-hover:translate-x-2 transition-all ease-in-out duration-300"
      ></span>
    </button>
  {:else}
    <div />
  {/if}
</div>
