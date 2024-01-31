<script>
  import { goto } from "$app/navigation";

  function searchButton() {}

  let search = "";
</script>

<nav
  class="my-6 mt-9 px-10 flex flex-row items-center justify-between text-black font-semibold shadow pb-4"
>
  <a class="" href="https://sacda.ca/index.php">
    <img
      src="https://sacda.ca/themes/sacda/assets/pawtucket/graphics/logo.svg"
      alt=""
      class="w-64"
    />
  </a>

  <button class="lg:hidden">
    <span class="fa fa-bars"></span>
    <span class="my-1 mx-2 close">X</span>
  </button>

  <div class="flex flex-col items-end gap-4">
    <div class="flex flex-row gap-4 items-center">
      <div class="flex">
        <input
          class="border border-black px-3 py-2 outline-none"
          placeholder="Search"
          bind:value={search}
        />
        <a
          href={"https://sacda.ca/index.php/MultiSearch/Index?search=" + search}
          class="bg-[#414042] border border-[#414042] hover:bg-[#F99D2A] text-[#FFEDC2] text-lg w-16 transition-all ease-in-out duration-200 flex items-center justify-center"
          type="button"
        >
          >
        </a>
      </div>
      <a
        class="lg:bg-[#414042] lg:hover:bg-[#F99D2A] lg:text-white lg:py-2 lg:px-6"
        href="https://sacda.ca/index.php/Search/advanced/objects"
        role="button">ADVANCED SEARCH</a
      >
    </div>

    <ul class="flex flex-row gap-4 items-center">
      <li class="nav-item">
        <a class="nav-link" href="https://sacda.ca/index.php/Browse/objects"
          >BROWSE
        </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://sacda.ca/index.php/Collections/index"
          >COLLECTIONS</a
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
        class="lg:bg-[#F99D2A] lg:py-2 lg:px-6 lg:hover:bg-[#414042] lg:hover:text-white transition-all ease-in-out duration-200"
      >
        <a
          class="nav-link"
          href="https://sacda.ca/index.php/Contribute/Artworks">CONTRIBUTE</a
        >
      </li>
    </ul>
  </div>
</nav>
