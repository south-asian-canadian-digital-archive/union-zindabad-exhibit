<script lang="ts">
  import { goto } from "$app/navigation";
  import { scale, slide } from "svelte/transition";

  function searchButton() {}

  let search = "";
  let mobileNavButtonWidth: number;

  $: mobileNavOpen = false;

  $: {
    mobileNavButtonWidth;
  }
</script>

<nav
  class="lg:h-24 md:h-24 my-6 mt-9 px-10 flex lg:flex-row md:flex-row flex-col items-center justify-between text-black font-semibold"
>
  <div class="w-full lg:w-fit md:w-fit">
    <a class="" href="https://sacda.ca/index.php">
      <img
        src="https://sacda.ca/themes/sacda/assets/pawtucket/graphics/logo.svg"
        alt=""
        class="w-64"
      />
    </a>

    <button
      class="lg:hidden md:hidden bg-[#F99D2A] py-10 px-8 absolute right-10 top-0"
      bind:clientWidth={mobileNavButtonWidth}
      on:click={() => (mobileNavOpen = !mobileNavOpen)}
    >
      {#if mobileNavOpen}
        <span class="fa fa-times scale-150"></span>
      {:else}
        <span class="fa fa-bars scale-150"></span>
      {/if}
    </button>
  </div>

  {#if mobileNavButtonWidth == 0 || mobileNavOpen}
    <div transition:slide class="md:flex lg:flex flex-col items-end gap-4">
      <div class="flex flex-row gap-4 items-center py-8 md:py-0 lg:py-0">
        <div class="flex">
          <input
            class="border border-black px-3 py-2 outline-none"
            placeholder="Search"
            bind:value={search}
          />
          <a
            href={"https://sacda.ca/index.php/MultiSearch/Index?search=" +
              search}
            class="bg-[#414042] border border-[#414042] hover:bg-[#F99D2A] text-[#FFEDC2] text-lg w-16 transition-all ease-in-out duration-200 flex items-center justify-center"
            type="button"
          >
            >
          </a>
        </div>
        <a
          class="lg:bg-[#414042] lg:hover:bg-[#F99D2A] lg:text-white lg:py-2 lg:px-6 md:bg-[#414042] md:hover:bg-[#F99D2A] md:text-white md:py-2 md:px-6 hidden md:flex lg:flex"
          href="https://sacda.ca/index.php/Search/advanced/objects"
          role="button">ADVANCED SEARCH</a
        >
      </div>

      <ul class="flex lg:flex-row md:flex-row flex-col gap-4 items-center">
        <li class="nav-item">
          <a class="nav-link" href="https://sacda.ca/index.php/Browse/objects"
            >BROWSE
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            href="https://sacda.ca/index.php/Collections/index">COLLECTIONS</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://sacda.ca/index.php/exhibits/index"
            >EXHIBITS</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://sacda.ca/index.php/About/Index"
            >ABOUT</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://sacda.ca/index.php/Contact/Form"
            >CONTACT</a
          >
        </li>
        <li
          class="lg:bg-[#F99D2A] lg:py-2 lg:px-6 lg:hover:bg-[#414042] lg:hover:text-white transition-all ease-in-out duration-200 md:bg-[#F99D2A] md:py-2 md:px-6 md:hover:bg-[#414042] md:hover:text-white"
        >
          <a
            class="nav-link"
            href="https://sacda.ca/index.php/Contribute/Artworks">CONTRIBUTE</a
          >
        </li>
        <li class="nav-item lg:hidden md:hidden">
          <a
            class="nav-link"
            href="https://sacda.ca/index.php/Search/advanced/objects"
            >ADVANCED SEARCH</a
          >
        </li>
      </ul>
    </div>
  {/if}
</nav>
